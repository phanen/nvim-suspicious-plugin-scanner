# Neovim Suspicious Plugin Scanner

Scans the `store.nvim` plugin database and flags suspicious plugins.

- Raw JSON report: [report.json](https://raw.githubusercontent.com/phanen/nvim-suspicious-plugin-scanner/master/report.json)

- Last updated: `2026-10-15T06:41:52+00:00`
- Database: [https://github.com/alex-popov-tech/store.nvim.crawler/releases/latest/download/db_minified.json](https://github.com/alex-popov-tech/store.nvim.crawler/releases/latest/download/db_minified.json)
- GitHub plugins scanned: `6906`
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

- `afewyards/codereview.nvim`: `HTTP Error 404: Not Found`
- `Anderson-Vilela-op/procman.nvim`: `HTTP Error 404: Not Found`
- `chewbakartik/editorfold.nvim`: `HTTP Error 404: Not Found`
- `dmshvedchenko/persist.nvim`: `HTTP Error 404: Not Found`
- `DrKJeff16/pipenv.nvim`: `GithubException: 409 {'message': 'Git Repository is empty.', 'documentation_url': 'https://docs.github.com/rest/commits/commits#get-a-commit', 'status': '409'}`
- `grapp-dev/nui-components.nvim`: `HTTP Error 404: Not Found`
- `hamzamogni/zed_onedark.nvim`: `HTTP Error 404: Not Found`
- `hase808/neovim-gitlab-snippets`: `HTTP Error 404: Not Found`
- `jmbuhr/otter.nvim`: `HTTP Error 404: Not Found`
- `kyoh86/denops-zenn_dev.vim`: `HTTP Error 404: Not Found`
- `maralla/completor.vim`: `HTTP Error 404: Not Found`
- `nvim-neotest/neotest`: `HTTP Error 404: Not Found`
- `nvim-telescope/telescope-fzf-native.nvim`: `HTTP Error 404: Not Found`
- `refractalize/oil-git-status.nvim`: `HTTP Error 404: Not Found`
- `stykhomyrov/vim-glsl`: `HTTP Error 404: Not Found`
- `tenxsoydev/karen-yank.nvim`: `HTTP Error 404: Not Found`

</details>
