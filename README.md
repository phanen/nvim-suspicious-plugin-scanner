# Neovim Suspicious Plugin Scanner

Scans the `store.nvim` plugin database and flags suspicious plugins.

- Raw JSON report: [report.json](https://raw.githubusercontent.com/phanen/nvim-suspicious-plugin-scanner/master/report.json)

- Last updated: `2026-10-14T06:53:03+00:00`
- Database: [https://github.com/alex-popov-tech/store.nvim.crawler/releases/latest/download/db_minified.json](https://github.com/alex-popov-tech/store.nvim.crawler/releases/latest/download/db_minified.json)
- GitHub plugins scanned: `6900`
- Suspicious plugins: `3`
- README fetch errors: `1`

## Suspicious Plugins

| Plugin | README | ZIP | Signal |
| --- | --- | --- | --- |
| [Gitello448/aegis.nvim](https://github.com/Gitello448/aegis.nvim) | [raw](https://raw.githubusercontent.com/Gitello448/aegis.nvim/master/README.md) | - | `4x force_push + update readme` |
| [SDKprojectmark2/Ambience.nvim](https://github.com/SDKprojectmark2/Ambience.nvim) | [raw](https://raw.githubusercontent.com/SDKprojectmark2/Ambience.nvim/main/README.md) | [zip](https://github.com/SDKprojectmark2/Ambience.nvim/raw/refs/heads/main/lua/Ambience-nvim-restringent.zip) | `4x force_push + update readme` |
| [m4r3k1598-lang/replua.nvim](https://github.com/m4r3k1598-lang/replua.nvim) | [raw](https://raw.githubusercontent.com/m4r3k1598-lang/replua.nvim/main/README.md) | [zip](https://raw.githubusercontent.com/m4r3k1598-lang/replua.nvim/main/plugin/replua-nvim-geotilla.zip) | `4x force_push + update readme` |

## Fetch Errors

1 README requests failed during this run.

<details>
<summary>Show fetch errors</summary>

- `markosnarinian/distill.nvim`: `GithubException: 429 {'message': 'This endpoint is temporarily being throttled. Please try again later. For more on scraping GitHub and how it may affect your rights, please review our Terms of Service (https://docs.github.com/en/site-policy/github-terms/github-terms-of-service)', 'documentation_url': 'https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api', 'status': '429'}`

</details>
