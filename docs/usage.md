# Using the pack

Take a pinned release (`rs-tech-brandstyle-<version>.tar.gz`, checked
against its `SHA256SUMS`), unpack it, and mount or copy the part each app
needs. Never edit the unpacked files: change `src/` here and release again.

Paths below are inside `rs-tech-brandstyle/` of the tarball. Status says
whether it has been tried on a running app.

## The zone's own pages

Status: built for it, not yet linked from rs-tech-infra.

Serve `css/zone.css`, `icons/` and `images/` next to the pages, and link them:

```html
<link rel="stylesheet" href="/brand/css/zone.css">
<link rel="icon" href="/brand/icons/favicon.ico">
<link rel="apple-touch-icon" href="/brand/icons/icon-180.png">
```

`zone.css` has the classes of rs-tech-infra's Matrix welcome page
(`main`, `.muted`, `.grid`, `.card`, `.for`, `.name`, `.note`, `footer`),
plus `.brand` (a logo at the top) and `.button`. The page's own `:root`
colour block goes away. `data-theme="light|dark"` on `<html>` forces a
scheme; without it the visitor's choice is followed.

Any other web project can use `css/tokens.css` alone: the variables
`--rs-bg`, `--rs-surface`, `--rs-fg`, `--rs-muted`, `--rs-line`,
`--rs-accent`, `--rs-accent-hover`, `--rs-accent-fg`, `--rs-accent-soft`
follow the scheme; `--rs-light-*` and `--rs-dark-*` are fixed; each has an
`-rgb` twin (`177 16 32`) for `rgb(var(--rs-accent-rgb) / .3)`. The
palette itself is `--rs-<family>-<shade>`: `night-950`…`600`, `gray-50`…`800`,
`white-100`, `red-50`…`900`, `crimson-50`…`900`; `--rs-highlight` is the
crimson accent.

Images and media of the pack are all rights reserved (`NOTICE.md`): fine for
our own pages, not for others to reuse.

## The nexus and data reading

Status: in the Blogger and Tumblr themes; seen in `docs/preview-nexus.html`.

`css/nexus.css` (tokens included) is the terminal look of the author's
"Technomantic Nexus" drafts as opt-in classes: `rs-frame` and `rs-status`
(the red frame and its status lines), `rs-nexus` with `rs-nav`/`rs-nav-hex`,
`main` and `rs-sidebar` (one column under 64rem), `rs-fragment`,
`rs-fragment-id`, `rs-title`, `rs-content`, backgrounds `rs-grid-bg`,
`rs-dots`, `rs-scanline`, a skip link `rs-skip`, and data blocks `rs-feed`,
`rs-tiles`. Motion stops under `prefers-reduced-motion`.

`js/rs-data.js` fills a list or tiles from public JSON (e.g. what gitrecon
gathers into `redscope-pl/.github`), described by `data-rs-*` attributes:

```html
<ul class="rs-feed" data-rs-src="https://raw.githubusercontent.com/redscope-pl/.github/master/data/events.json"
    data-rs-title="repo.name" data-rs-url="repo.url" data-rs-date="created_at" data-rs-kind="type">
  <li>What shows without script or data.</li>
</ul>
<script src="/brand/js/rs-data.js"></script>
```

It writes text, never HTML; links only `http(s)`; `aria-busy` while loading;
a `role="status"` note when the data can't be read, keeping what was there.
`js/rs-scramble.js` settles the letters of `data-rs-scramble` elements out
of noise; screen readers get the real words, reduced motion gets none of it.
(The address above is an example: the data's place is not decided, Q12.)

## Authentik

Status: not yet tried (rs-tech-infra TODO Phase 8).

- `authentik/custom.css`: the brand's custom CSS (`branding_custom_css`
  in a brand blueprint, its content as the value).
- `images/logo/logo-dark.svg` as `branding_logo`, `icons/favicon.ico` as
  `branding_favicon`, `authentik/flow-background.svg` as
  `branding_default_flow_background`: served by Authentik from a mounted
  folder (e.g. `/web/dist/assets/rs-tech/`).

## Gitea

Status: not yet tried.

Mount `gitea/public/` as `$GITEA_CUSTOM/public/` (in the official image
`/data/gitea/public/`). Gitea finds the themes by their file names; make one
the default:

```ini
[ui]
DEFAULT_THEME = redscope-auto
```

The logos replace Gitea's (`public/assets/img/logo.svg`, `favicon.svg`,
…). The themes import Gitea's own `theme-gitea-light.css` /
`theme-gitea-dark.css` and change only colours and fonts, so they survive
Gitea upgrades as long as those files keep their names.

## Vaultwarden

Status: not yet tried.

Mount `vaultwarden/templates/` and set `TEMPLATES_FOLDER` to it (Vaultwarden
1.33 or later). Vaultwarden adds `scss/user.vaultwarden.scss.hbs` after its
own CSS. The web vault's variable names change between versions: check
the colours after each upgrade.

## Not covered yet

The Matrix web client (Cinny) has no way to load outside themes; see
[TODO](devlog/TODO.md).
