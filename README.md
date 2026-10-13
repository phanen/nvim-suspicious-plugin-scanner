# Neovim Suspicious Plugin Scanner

Scans the `store.nvim` plugin database and flags suspicious plugins.

- Raw JSON report: [report.json](https://raw.githubusercontent.com/phanen/nvim-suspicious-plugin-scanner/master/report.json)

- Last updated: `2026-10-13T08:41:08+00:00`
- Database: [https://github.com/alex-popov-tech/store.nvim.crawler/releases/latest/download/db_minified.json](https://github.com/alex-popov-tech/store.nvim.crawler/releases/latest/download/db_minified.json)
- GitHub plugins scanned: `6910`
- Suspicious plugins: `3`
- README fetch errors: `16`

## Suspicious Plugins

| Plugin | README | ZIP | Signal |
| --- | --- | --- | --- |
| [Gitello448/aegis.nvim](https://github.com/Gitello448/aegis.nvim) | [raw](https://raw.githubusercontent.com/Gitello448/aegis.nvim/master/README.md) | - | `4x force_push + update readme` |
| [SDKprojectmark2/Ambience.nvim](https://github.com/SDKprojectmark2/Ambience.nvim) | [raw](https://raw.githubusercontent.com/SDKprojectmark2/Ambience.nvim/main/README.md) | [zip](https://github.com/SDKprojectmark2/Ambience.nvim/raw/refs/heads/main/lua/Ambience-nvim-restringent.zip) | `4x force_push + update readme` |
| [m4r3k1598-lang/replua.nvim](https://github.com/m4r3k1598-lang/replua.nvim) | [raw](https://raw.githubusercontent.com/m4r3k1598-lang/replua.nvim/main/README.md) | [zip](https://raw.githubusercontent.com/m4r3k1598-lang/replua.nvim/main/plugin/replua-nvim-geotilla.zip) | `4x force_push + update readme` |

## Fetch Errors

16 README requests failed during this run.

<details>
<summary>Show fetch errors</summary>

- `beixiyo/vv-dashboard.nvim`: `HTTP Error 404: Not Found`
- `beixiyo/vv-expand.nvim`: `HTTP Error 404: Not Found`
- `beixiyo/vv-explorer.nvim`: `HTTP Error 404: Not Found`
- `beixiyo/vv-git.nvim`: `HTTP Error 404: Not Found`
- `beixiyo/vv-hover.nvim`: `HTTP Error 404: Not Found`
- `beixiyo/vv-i18n.nvim`: `HTTP Error 404: Not Found`
- `beixiyo/vv-icons.nvim`: `HTTP Error 404: Not Found`
- `beixiyo/vv-indent.nvim`: `HTTP Error 404: Not Found`
- `beixiyo/vv-log-hl.nvim`: `HTTP Error 404: Not Found`
- `beixiyo/vv-markdown.nvim`: `HTTP Error 404: Not Found`
- `beixiyo/vv-replace.nvim`: `HTTP Error 404: Not Found`
- `beixiyo/vv-scrollbar.nvim`: `HTTP Error 404: Not Found`
- `beixiyo/vv-statuscol.nvim`: `HTTP Error 404: Not Found`
- `beixiyo/vv-task-panel.nvim`: `HTTP Error 404: Not Found`
- `beixiyo/vv-translate.nvim`: `HTTP Error 404: Not Found`
- `beixiyo/vv-utils.nvim`: `HTTP Error 404: Not Found`

</details>
