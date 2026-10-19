# TODO

What is being worked on now. Questions: [BRAINSTORM.md](BRAINSTORM.md).

## Phase 1: the pack exists (2026-10-19)

- [x] Rewrite from the template: BOS anatomy, tooling of rs-tech-infra
      (uv, go-task, commitizen, lefthook, yamllint), CI `task check`
- [x] One source of colours, fonts, radii: `src/tokens.json`, WCAG AA
      contrast checked in both schemes
- [x] The logo as vectors: the eye and the words traced from the PNGs of
      the site (`src/logo/`), lockups light and dark, icons, favicon
- [x] Themes: the zone's pages (`zone.css`), Authentik, Gitea, Vaultwarden
- [x] Reproducible build and tarball with `MANIFEST.sha256`; release
      workflow on tags `v*`
- [ ] The author looks at the pack (`task preview`) and confirms or
      corrects colours and the traced logo (Q2, Q3)
- [ ] Licence settled (Q1), then the first release `v0.1.0` (needs the
      author's go-ahead: tag + push)

**Done when:** a tagged release exists and rs-tech-infra can pin it.

## Phase 2: on the zone (with rs-tech-infra TODO Phase 8)

- [ ] Each theme tried on the running app, `docs/usage.md` status updated:
      Authentik, Gitea, Vaultwarden, the Matrix welcome page
- [ ] Error pages (`400`…`503`) for `www.redscope.pl` styled from the
      pack (the site's own work, forge note)
- [ ] The Matrix web client (Cinny): a way to brand it, or a decision not to

**Done when:** every page a member sees carries the style.

## Later

- [ ] A brand font (Q4)
- [ ] An npm package of `css/` and `logo/` for web projects like the
      redscope.pl site (Q5)
