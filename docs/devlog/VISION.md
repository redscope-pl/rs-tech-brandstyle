# VISION

From the author's vision draft (orders, 2026-10-19; word for word in
`docs/changelog/phase-1.md`).

RedScope Technologies looks the same wherever it shows up, and starting
something new in that look takes minutes, not a redesign. This repository is
where the look lives and from where it propagates:

1. **The brand and its notice.** The logo, the name, the palette (dark night
   with gray, white, red and crimson, in shades), and the notices that
   protect them: copyright, trademark, all rights reserved on images and
   media. Written once, reusable by every project (`docs/legal/`).
2. **A basic style pack with starting packets** for the places we publish:
   - documentation on **GitBook** and **Read the Docs**
   - sites on **GitHub Pages** built with **Vue**, **React** or **Astro**
   - blogs on **Tumblr** and **Blogger** (themes)
3. **Customizations for the infra project** (rs-tech-infra): every page a
   member of the zone sees carries the style: Authentik, Gitea,
   Vaultwarden, the Matrix pages, the error pages.

Principles:

- One source (`src/tokens.json`, `resources/`); everything else is built
  from it and pinned by version and hash.
- Code and stylesheets open (MPL-2.0); images and brand signs ours (all
  rights reserved).
- Nothing loaded from third parties on our pages; fonts are the system's
  own, terminal-like.
- The logo and lettering will change (similar, not the same): nothing may
  depend on the current drawing beyond its master files.
- A theme counts as done when it was seen working on the real platform.
