# rs-tech-brandstyle

The RedScope Technologies style pack: the logo, colours and fonts as files,
and ready themes for the software of the zone (Authentik, Gitea, Vaultwarden,
the zone's own pages). One source, `src/tokens.json` and `resources/`; one build; one pinned
release that other projects pull, so the brand propagates without copying by
hand.

## What's in the pack

`task build` makes `dist/rs-tech-brandstyle/` and
`dist/rs-tech-brandstyle-<version>.tar.gz` (reproducible, listed in
`MANIFEST.sha256`):

| Path                         | What it is                                                     |
| ---------------------------- | -------------------------------------------------------------- |
| `css/tokens.css`             | The palette (night, gray, white, red, crimson in shades), fonts, radii as CSS variables (`--rs-*`), light + dark |
| `css/zone.css`               | Base style of the zone's own HTML pages (tokens included)       |
| `images/logo/`               | The eye (`mark.svg`), the words, both together (light, dark)    |
| `icons/`                     | App icons, favicons (PNG, ICO), the eye as a transparent PNG    |
| `images/backgrounds/`        | Backgrounds (Authentik's flows)                                 |
| `authentik/`                 | The brand's custom CSS and a flow background                   |
| `gitea/public/`              | Themes `redscope-auto/light/dark` and logos, for Gitea's `custom/` |
| `vaultwarden/templates/`     | The web vault's own CSS                                        |
| `LICENSE`, `NOTICE.md`, `legal/` | MPL-2.0 for the code; images all rights reserved; copyright and trademark notices |

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
variables, never colour values. Images live in `resources/`; after changing
a master (`resources/images/logo/mark.svg`, `wordmark.svg`, the source PNGs)
or the palette, run `uv run task resources` and commit what it redraws.

## Releases

A tag `v<version>` (made with `uv run cz bump`) builds the pack on GitHub and
attaches the tarball and its `SHA256SUMS` to a release. Consumers pin the
tarball by version and hash.

## Licence

- Code, stylesheets, configuration and docs: Mozilla Public License 2.0
  ([LICENSE](LICENSE)).
- Images and media (`resources/`): all rights reserved
  ([resources/NOTICE.md](resources/NOTICE.md)).
- The name and logo of RedScope Technologies: see
  [docs/legal/TRADEMARK.md](docs/legal/TRADEMARK.md); a code licence gives
  no right to them.

© 2025–2026 RedScope Technologies, author
[Sett Sarverott A.A.B.](https://orcid.org/0009-0006-4604-6540)
([docs/legal/COPYRIGHT.md](docs/legal/COPYRIGHT.md)).
