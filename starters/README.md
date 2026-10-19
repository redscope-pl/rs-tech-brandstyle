# Starters

Starting packets in the RedScope style, one per place we publish (VISION,
TODO Phase 3). Take them from a built pack (`dist/rs-tech-brandstyle/starters/`
or a release tarball): there the brand is already put in. The sources in the
repository's `starters/` lack it (placeholders `@@RS_…@@`, no `brand/`).

| Starter    | For                                   | Take it                                   |
| ---------- | ------------------------------------- | ----------------------------------------- |
| `sphinx/`  | Read the Docs (Sphinx, Furo theme)    | copy as the docs folder of a project      |
| `gitbook/` | GitBook                               | enter the values of its README, upload `brand/` files |
| `tumblr/`  | redscope.tumblr.com (images)          | paste `theme.html` into Edit theme → Edit HTML |
| `blogger/` | blog.redscope.online (articles, news) | Theme → Restore/Edit HTML with `theme.xml` |
| `vue/`     | GitHub Pages, Vue                     | copy as a new repository, `npm ci`, push  |
| `react/`   | GitHub Pages, React                   | copy as a new repository, `npm ci`, push  |
| `astro/`   | GitHub Pages, Astro                   | copy as a new repository, `npm ci`, push  |

Images and media inside (`brand/`) are all rights reserved
(`brand/NOTICE.md`); the code of the starters is MPL-2.0. Each starter's own
README says what was tried on the real platform.
