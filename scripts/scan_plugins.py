#!/usr/bin/env python3

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass

DB_URL = (
    "https://github.com/alex-popov-tech/store.nvim.crawler/releases/latest/"
    "download/db_minified.json"
)
README_PATH = "README.md"
REQUEST_TIMEOUT = 20
RETRY_COUNT = 3
USER_AGENT = "nvim-suspicious-plugin-scanner/1.0"
ZIP_URL_RE = re.compile(
    r"https?://[^\s<>'\"`\])]+?\.zip(?:[?#][^\s<>'\"`)]*)?",
    re.IGNORECASE,
)
VERSION_TOKEN_RE = re.compile(
    r"(?:^|[._-])v?\d+(?:\.\d+){0,3}(?:[._-]?(?:alpha|beta|rc)\d*)?(?:$|[._-])",
    re.IGNORECASE,
)
IGNORED_URL_PATTERNS = (
    re.compile(
        r"^https://sourceforge\.net/projects/gnuwin32/files/make/[^/]+/[^/]+\.zip$",
        re.IGNORECASE,
    ),
    re.compile(
        r"^https://github\.com/ryanoasis/nerd-fonts/releases/download/[^/]+/[^/]+\.zip$",
        re.IGNORECASE,
    ),
)


@dataclass(frozen=True)
class Plugin:
    full_name: str
    url: str
    readme_ref: str
    readme_url: str


@dataclass(frozen=True)
class Finding:
    plugin: Plugin
    zip_links: tuple[str, ...]


@dataclass(frozen=True)
class FetchError:
    plugin: Plugin
    error: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan store.nvim plugin READMEs for suspicious .zip links."
    )
    parser.add_argument("--db-url", default=DB_URL, help="Plugin database URL")
    parser.add_argument(
        "--readme-path",
        default=README_PATH,
        help="Path of the generated README file",
    )
    parser.add_argument(
        "--workers",
        type=int,
        help="Concurrent README fetch workers; auto-detected when omitted",
    )
    return parser.parse_args()


def choose_worker_count() -> int:
    cpu_count = os.cpu_count() or 4
    is_ci = os.environ.get("CI", "").lower() in {"1", "true", "yes"}

    # README fetching is network-bound, so use a higher multiplier than CPU count
    # while keeping the pool bounded for GitHub and CI runner stability.
    multiplier = 8 if is_ci else 6
    floor = 16 if is_ci else 8
    ceiling = 64 if is_ci else 48
    return max(floor, min(ceiling, cpu_count * multiplier))


def fetch_text(url: str, timeout: int = REQUEST_TIMEOUT) -> str:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme in ("", "file"):
        path = parsed.path if parsed.scheme == "file" else url
        with open(os.path.expanduser(path), encoding="utf-8") as handle:
            return handle.read()

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json, text/plain, text/markdown;q=0.9, */*;q=0.8",
    }
    request = urllib.request.Request(url, headers=headers)

    last_error: Exception | None = None
    for attempt in range(1, RETRY_COUNT + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                charset = response.headers.get_content_charset() or "utf-8"
                return response.read().decode(charset, errors="replace")
        except (TimeoutError, urllib.error.HTTPError, urllib.error.URLError) as exc:
            last_error = exc
            if attempt == RETRY_COUNT:
                break
            time.sleep(min(2 ** (attempt - 1), 4))

    assert last_error is not None
    raise last_error


def normalize_readme_ref(readme_ref: str) -> str:
    return readme_ref.lstrip("/")


def build_raw_readme_url(full_name: str, readme_ref: str) -> str:
    return f"https://raw.githubusercontent.com/{full_name}/{normalize_readme_ref(readme_ref)}"


def load_plugins(db_url: str) -> list[Plugin]:
    payload = json.loads(fetch_text(db_url))
    items = payload.get("items", [])

    plugins: list[Plugin] = []
    for item in items:
        if item.get("source") != "github":
            continue

        full_name = item.get("full_name")
        url = item.get("url")
        readme_ref = item.get("readme")
        if not isinstance(full_name, str) or not isinstance(url, str):
            continue
        if not isinstance(readme_ref, str) or not readme_ref.strip():
            continue

        plugins.append(
            Plugin(
                full_name=full_name,
                url=url,
                readme_ref=normalize_readme_ref(readme_ref),
                readme_url=build_raw_readme_url(full_name, readme_ref),
            )
        )

    return plugins


def is_ignored_url(url: str) -> bool:
    return any(pattern.search(url) for pattern in IGNORED_URL_PATTERNS)


def extract_zip_links(readme_text: str) -> tuple[str, ...]:
    seen: set[str] = set()
    links: list[str] = []
    for match in ZIP_URL_RE.findall(readme_text):
        cleaned = match.rstrip(".,;:!?")
        path = urllib.parse.urlparse(cleaned).path
        filename = path.rsplit("/", 1)[-1]
        if not filename.lower().endswith(".zip"):
            continue
        basename = filename[:-4]
        if not VERSION_TOKEN_RE.search(basename):
            continue
        if is_ignored_url(cleaned):
            continue
        if cleaned not in seen:
            seen.add(cleaned)
            links.append(cleaned)
    return tuple(links)


def scan_plugin(plugin: Plugin) -> Finding | FetchError | None:
    try:
        readme_text = fetch_text(plugin.readme_url)
    except Exception as exc:
        return FetchError(plugin=plugin, error=str(exc))

    zip_links = extract_zip_links(readme_text)
    if not zip_links:
        return None
    return Finding(plugin=plugin, zip_links=zip_links)


def scan_plugins(plugins: list[Plugin], workers: int) -> tuple[list[Finding], list[FetchError]]:
    findings: list[Finding] = []
    errors: list[FetchError] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_map = {executor.submit(scan_plugin, plugin): plugin for plugin in plugins}
        for index, future in enumerate(concurrent.futures.as_completed(future_map), start=1):
            result = future.result()
            if isinstance(result, Finding):
                findings.append(result)
            elif isinstance(result, FetchError):
                errors.append(result)

            if index % 100 == 0 or index == len(plugins):
                print(
                    f"processed {index}/{len(plugins)} plugins",
                    file=sys.stderr,
                )

    findings.sort(key=lambda item: item.plugin.full_name.lower())
    errors.sort(key=lambda item: item.plugin.full_name.lower())
    return findings, errors


def render_findings(findings: list[Finding]) -> str:
    if not findings:
        return "No suspicious `.zip` links found.\n"

    lines = [
        "| Plugin | README | ZIP |",
        "| --- | --- | --- |",
    ]
    for finding in findings:
        for link in finding.zip_links:
            lines.append(
                f"| [{finding.plugin.full_name}]({finding.plugin.url}) | "
                f"[raw]({finding.plugin.readme_url}) | "
                f"[zip]({link}) |"
            )

    return "\n".join(lines).rstrip() + "\n"


def render_errors(errors: list[FetchError]) -> str:
    if not errors:
        return ""

    lines = [
        "## Fetch Errors",
        "",
        f"{len(errors)} README requests failed during this run.",
        "",
        "<details>",
        "<summary>Show fetch errors</summary>",
        "",
    ]
    for item in errors:
        lines.append(f"- `{item.plugin.full_name}`: `{item.error}`")
    lines.extend(["", "</details>", ""])
    return "\n".join(lines)


def render_readme(
    *,
    db_url: str,
    plugins: list[Plugin],
    findings: list[Finding],
    errors: list[FetchError],
) -> str:
    scanned_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    body = render_findings(findings)
    error_block = render_errors(errors)

    lines = [
        "# Neovim Suspicious Plugin Scanner",
        "",
        "Scans the `store.nvim` plugin database and flags GitHub READMEs that contain direct `.zip` download links.",
        "",
        f"- Last updated: `{scanned_at}`",
        f"- Database: [{db_url}]({db_url})",
        f"- GitHub plugins scanned: `{len(plugins)}`",
        f"- Suspicious plugins: `{len(findings)}`",
        f"- README fetch errors: `{len(errors)}`",
        "",
        "## Suspicious Plugins",
        "",
        body.rstrip(),
        "",
    ]

    if error_block:
        lines.append(error_block.rstrip())
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_readme(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def main() -> int:
    args = parse_args()
    workers = max(1, args.workers) if args.workers else choose_worker_count()

    print(f"loading plugin database from {args.db_url}", file=sys.stderr)
    plugins = load_plugins(args.db_url)
    print(f"loaded {len(plugins)} github plugins", file=sys.stderr)
    print(f"using {workers} concurrent workers", file=sys.stderr)

    findings, errors = scan_plugins(plugins, workers)
    readme = render_readme(
        db_url=args.db_url,
        plugins=plugins,
        findings=findings,
        errors=errors,
    )
    write_readme(args.readme_path, readme)
    print(
        f"wrote {args.readme_path} with {len(findings)} suspicious plugins",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
