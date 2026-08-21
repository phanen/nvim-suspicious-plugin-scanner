# Neovim Suspicious Plugin Scanner

Scans the `store.nvim` plugin database and flags suspicious plugins.

- Raw JSON report: [report.json](https://raw.githubusercontent.com/phanen/nvim-suspicious-plugin-scanner/master/report.json)

- Last updated: `2026-08-21T02:54:17+00:00`
- Database: [https://github.com/alex-popov-tech/store.nvim.crawler/releases/latest/download/db_minified.json](https://github.com/alex-popov-tech/store.nvim.crawler/releases/latest/download/db_minified.json)
- GitHub plugins scanned: `6676`
- Suspicious plugins: `4`
- README fetch errors: `1`

## Suspicious Plugins

| Plugin | README | ZIP | Signal |
| --- | --- | --- | --- |
| [Gitello448/aegis.nvim](https://github.com/Gitello448/aegis.nvim) | [raw](https://raw.githubusercontent.com/Gitello448/aegis.nvim/master/README.md) | - | `4x force_push + update readme` |
| [SDKprojectmark2/Ambience.nvim](https://github.com/SDKprojectmark2/Ambience.nvim) | [raw](https://raw.githubusercontent.com/SDKprojectmark2/Ambience.nvim/main/README.md) | [zip](https://github.com/SDKprojectmark2/Ambience.nvim/raw/refs/heads/main/lua/Ambience-nvim-restringent.zip) | `4x force_push + update readme` |
| [basel184/nvim-pretty-ts-errors](https://github.com/basel184/nvim-pretty-ts-errors) | [raw](https://raw.githubusercontent.com/basel184/nvim-pretty-ts-errors/main/README.md) | [zip](https://raw.githubusercontent.com/basel184/nvim-pretty-ts-errors/main/rplugin/ts_pretty_nvim_errors_v3.5.zip) | `versioned zip` |
| [m4r3k1598-lang/replua.nvim](https://github.com/m4r3k1598-lang/replua.nvim) | [raw](https://raw.githubusercontent.com/m4r3k1598-lang/replua.nvim/main/README.md) | [zip](https://raw.githubusercontent.com/m4r3k1598-lang/replua.nvim/main/plugin/replua-nvim-geotilla.zip) | `4x force_push + update readme` |

## Fetch Errors

1 README requests failed during this run.

<details>
<summary>Show fetch errors</summary>

- `timothyckl/tau.nvim`: `GithubException: 422 {'message': 'No commit found for SHA: 0000000000000000000000000000000000000000', 'documentation_url': 'https://docs.github.com/rest/commits/commits#get-a-commit', 'status': '422'}`

</details>
