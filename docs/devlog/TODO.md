# TODO

What is being worked on now. Vision: [VISION.md](VISION.md). Questions:
[BRAINSTORM.md](BRAINSTORM.md). History: [../changelog/](../changelog/).

## Phase 1: the pack exists

- [x] Rewrite from the template: BOS anatomy, tooling of rs-tech-infra
      (uv, go-task, commitizen, lefthook, yamllint), CI `task check`
- [x] One source of colours, fonts, radii: `src/tokens.json`, WCAG AA
      contrast checked in both schemes
- [x] The logo as vectors: the eye and the words traced from the PNGs of
      the site, lockups light and dark, icons, favicon
- [x] Themes: the zone's pages (`zone.css`), Authentik, Gitea, Vaultwarden
- [x] Reproducible build and tarball with `MANIFEST.sha256`; release
      workflow on tags `v*`
- [x] Licence settled (Q1): MPL-2.0 for code, images and media all rights
      reserved
- [x] The palette: night, gray, white, red, crimson in shades (Q2)
- [x] Images in `resources/` (icons, images, media apart), checked fresh;
      copyright and trademark notices in `docs/legal/`, carried by the pack (Q3)
- [ ] The author looks at the pack again (`task preview`): the palette, the
      traced logo
- [ ] The first release `v0.1.0`: `cz bump`, tag, push (needs the author's
      go-ahead)

**Done when:** a tagged release exists and rs-tech-infra can pin it.

## Phase 2: on the zone (with rs-tech-infra TODO Phase 8)

- [ ] Each theme tried on the running app, `docs/usage.md` status updated:
      Authentik, Gitea, Vaultwarden, the Matrix welcome page
- [ ] Error pages (`400`…`503`) for `www.redscope.pl` styled from the
      pack (the site's own work, forge note)
- [ ] The Matrix web client (Cinny): a way to brand it, or a decision not to

**Done when:** every page a member sees carries the style.

## Phase 3: starting packets (vision)

Where they live: Q6.

- [ ] GitHub Pages: a Vue, a React and an Astro starter with the pack's
      tokens, logo, favicon, light/dark
- [ ] Read the Docs: the theme of the chosen tool (Q7)
- [ ] GitBook: the brand settings and files, with a guide (Q8)
- [ ] Tumblr theme and Blogger theme (Q9)

**Done when:** each starter builds in CI and was seen on its platform.

## Later

- [ ] A brand font (Q4)
- [ ] An npm package of `css/` and the images for web projects like the
      redscope.pl site (Q5)
