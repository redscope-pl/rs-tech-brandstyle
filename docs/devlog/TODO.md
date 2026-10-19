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
- [x] The author looks at the pack again (`task preview`): "ready"
      (2026-10-19). The logo and lettering will be redrawn soon, similar but
      not the same (Q4)
- [x] Font: terminal-like monospace from the system's fonts (Q4); holder
      of rights: RedScope Technologies, author Sett Sarverott A.A.B. (Q10)
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

In `starters/<platform>/` here; each becomes a template repository once used
for real (Q6). `task build` makes them ready to use in
`dist/rs-tech-brandstyle/starters/`, with the pack's files put in.

- [ ] Read the Docs: Sphinx with Furo, `.readthedocs.yaml` (Q7)
- [ ] GitBook: the base customization, values and files to enter (Q8)
- [ ] Tumblr theme for `redscope.tumblr.com`, a blog of images (Q9)
- [ ] Blogger theme for `blog.redscope.online`, articles and news (Q9)
- [ ] GitHub Pages: a Vue, a React and an Astro starter with the pack's
      tokens, logo, favicon, light/dark, deployed by a Pages workflow
- [ ] `task check` builds every starter that can be built offline of its
      platform (Sphinx, Vue, React, Astro); Tumblr and Blogger checked
      for well-formedness

**Done when:** each starter builds in CI and was seen on its platform.

## Later

- [ ] npm packages for integrating the basic style, separate for Vue,
      React, Astro and vanilla web projects (Q5: not now)
- [ ] Read the Docs with MkDocs too (Q7)
- [ ] The new logo and lettering (Q4): replace the masters in
      `resources/images/logo/`, the crop constants in `scripts/build.py`,
      `task resources`
