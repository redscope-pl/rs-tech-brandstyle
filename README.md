# rs-tech-brandstyle

The RedScope Technologies style pack: the logo, colours and fonts as files,
and ready themes for the software of the zone (Authentik, Gitea, Vaultwarden,
the zone's own pages). One source, `src/tokens.json`; one build; one pinned
release that other projects pull, so the brand propagates without copying by
hand.

## What's in the pack

`task build` makes `dist/rs-tech-brandstyle/` and
`dist/rs-tech-brandstyle-<version>.tar.gz` (reproducible, listed in
`MANIFEST.sha256`):

| Path                         | What it is                                                     |
| ---------------------------- | -------------------------------------------------------------- |
| `css/tokens.css`             | Colours, fonts, radii as CSS variables (`--rs-*`), light + dark |
| `css/zone.css`               | Base style of the zone's own HTML pages (tokens included)       |
| `logo/`                      | The eye (`mark.svg`), the words, both together (light, dark), PNG icons, `favicon.ico` |
| `authentik/`                 | The brand's custom CSS and a flow background                   |
| `gitea/public/`              | Themes `redscope-auto/light/dark` and logos, for Gitea's `custom/` |
| `vaultwarden/templates/`     | The web vault's own CSS                                        |

How each app takes its part: [docs/usage.md](docs/usage.md).
`task preview` opens [docs/preview.html](docs/preview.html), a page showing
the built pack.

## Working on it

```sh
uv sync              # tools from PyPI: task, commitizen, lefthook, yamllint, Pillow
uv run task setup    # + git hooks
uv run task build    # dist/
uv run task check    # tokens, WCAG contrast, SVGs, two builds compared, YAML, commits (= CI)
```

Change colours in `src/tokens.json` only. App themes in `src/apps/` use the
variables, never colour values.

## Releases

A tag `v<version>` (made with `uv run cz bump`) builds the pack on GitHub and
attaches the tarball and its `SHA256SUMS` to a release. Consumers pin the
tarball by version and hash.

## Licence

Not settled yet ([BRAINSTORM Q1](docs/devlog/BRAINSTORM.md)): `LICENSE` is
the Mozilla Public License 2.0, while the README so far named
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
(© 2025 [Sett Sarverott A.A.B.](https://orcid.org/0009-0006-4604-6540)).
