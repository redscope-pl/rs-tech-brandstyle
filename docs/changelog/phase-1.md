# Phase 1: the pack exists

Decisions and history of Phase 1, append-only: sections are never rewritten;
each new one starts with `UNIXUSAT=<ms since epoch> · commit <hash>`.

## UNIXUSAT=1792440028962 · commit 79e1671

Phase 1 began with commit `79e1671`: the template rewritten as the style
pack (tokens, traced logo, themes for Authentik, Gitea, Vaultwarden and the
zone's pages, reproducible build, tooling of rs-tech-infra).

### The author's orders, first batch (word for word)

> ## what we work on - vision draft
>
> - branding and trademark notice of RedScope Technologies
> - basic stylization pack with starting packet
>     - gitbook
>     - readthedocs
>     - github pages in vue, react and astro
>     - tumblr theme
>     - blogger theme
> - customizations for infra project
>
> ---
>
> ### Q1
> - option `b)` in brainstorm sounds good.
>
> ### Q2
> colours should be variations of dark night with gray, white, red and crimson including shades
>
> ### Q3
> all images to "resources/*" with icons and else images and media files in separed dirs. all media are all rights reserved. in docs/ we should place copyright claim notice and other universal documents that we want to use in future.

### Answered questions (moved from BRAINSTORM.md word for word)

#### Q1: the licence

`LICENSE` is the Mozilla Public License 2.0; the old README named CC
BY-NC-SA 4.0; the old `pyproject.toml` said CC BY-SA 4.0. The pack holds
both code (build script, CSS) and the logo. rs-tech-infra asks whether the
licence fits pages of other software (Gitea, Authentik: MIT and others).

- a) MPL-2.0 for all of it
- b) MPL-2.0 for code and CSS, the logo all rights reserved (as a mark)
- c) CC BY-NC-SA 4.0 for all of it (non-commercial: awkward for an
  office's own commercial pages)

*Lean:* b): the CSS themes link into other software freely; the logo is
not something others should reuse.

**Decision:** option `b)` in brainstorm sounds good.

#### Q2: colours

Sampled from the logo: red `#b11020` on night `#160100`. Light scheme:
warm white `#fbf8f6`, links and buttons in the logo red. Dark scheme: the
logo's night as background, a lighter red `#f2444f` for links (the logo red
on night is too dark for text, 2.5:1).

*Lean:* keep them until the author corrects.

**Decision:** colours should be variations of dark night with gray, white, red and crimson including shades

#### Q3: the logo as vectors

The eye and the words in `src/logo/` are traced from the PNGs of the site
(1000 px logo, 809 px words). The eye is close; the words are smoothed from
a small, noisy PNG. Is there an original vector file (the designer's)?

*Lean:* use the traced ones until an original turns up; replace then.

**Decision:** all images to "resources/*" with icons and else images and media files in separed dirs. all media are all rights reserved. in docs/ we should place copyright claim notice and other universal documents that we want to use in future.

### What was done with them

- Q1: `LICENSE` (MPL-2.0) covers code and stylesheets; images and media
  are all rights reserved (`resources/NOTICE.md`).
- Q2: `src/tokens.json` is a palette (night, gray, white, red, crimson in
  shades); the light and dark schemes only name its shades. A second
  accent, `highlight`, is crimson.
- Q3: images moved to `resources/` (`icons/`, `images/logo/`,
  `images/backgrounds/`; `media/` when there is any). The icons and the
  light/dark logos are made from the masters there by `task resources` and
  committed; `task check` fails when they are stale. Reusable notices in
  `docs/legal/` (`COPYRIGHT.md`, `TRADEMARK.md`); the pack carries them.
- The vision draft became `docs/devlog/VISION.md`, and Phase 3 of TODO.
