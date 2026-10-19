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

## UNIXUSAT=1792442554488 · commit 17340c8

### The author's orders, second batch (word for word)

> ### Q4
> let's replace font into terminal-like basic that can be found in system's library of fonts. whole stuff like logo and logotyping will be soon changed but not yet - keep it inmind that it will be similar but not same.
>
> ### Q9
>
> - tumblr blog with images to be hosted:
>     - https://redscope.tumblr.com/
> - blogger blog with articles and news:
>     - origin url from blogger = `redscopetech.blogspot.com`
>     - changed to domain: https://blog.redscope.online/
>
> ### Q10
> copyright holder is me (e.g. Sett Sarverott A.A.B.) as the author, but i made it for my yet unregistered business "RedScope Technologies" - it still is in the middle of preparations to become commercial entity.
> We can make that as main holder of rights in here, later i will create holded by NFT ownership company shares.
> Either way
>
> ### Q7
> for readthedocs let's try Sphinx first. in future moves we gonna add mkdocs also.
>
> ### Q5
> add package for npm installations. we want to be able integrate basic stylization. we will gonna separate vue, react, astro and bare vanilla web projects approaches. but yea **not now** - keep it for later.
>
> ### Q8
> i see. then we will gonna just place there base customization.
>
> ### Q6
> yep, option `c)` fits for me

### Answered questions (moved from BRAINSTORM.md word for word)

#### Q4: a brand font

The words of the logo are lettering (a cut R, T, E), not a font the pages
can use. Pages use the system font now.

- a) system fonts (no files, nothing to load)
- b) a self-hosted open font close to the lettering (OFL)

*Lean:* a) until there is a reason.

**Decision:** see Q4 in the batch above.

#### Q5: npm package

The old `package.json` named the pack for npm. Publishing to npm is outward
and permanent.

*Lean:* not now; the tarball release is enough for the zone.

**Decision:** see Q5 in the batch above.

#### Q6: where the starting packets live

The vision asks for starting packets: GitBook, Read the Docs, GitHub Pages
(Vue, React, Astro), Tumblr, Blogger.

- a) here, `starters/<platform>/`, each minimal, built and checked with the pack
- b) one template repository per starter in the scope (GitHub "template
  repository"), each pulling a pinned pack release
- c) a) first, b) once a starter is used for real

*Lean:* c): one place to keep them in step while the pack changes fast.

**Decision:** see Q6 in the batch above.

#### Q7: Read the Docs: which documentation tool

Read the Docs builds Sphinx and MkDocs (and others). Each needs its own theme.

- a) MkDocs with Material (an `extra.css` and the logo)
- b) Sphinx with Furo (CSS variables, light and dark)
- c) both

*Lean:* a): Markdown like the rest of our docs; Material has light/dark and
takes CSS variables.

**Decision:** see Q7 in the batch above.

#### Q8: GitBook

Hosted GitBook takes the brand through its settings (primary colour, logo,
favicon, fonts from a list), not through CSS. The packet would be the values
and files to enter, and a guide.

*Lean:* that, unless there is a self-hosted GitBook (legacy CLI) in use.

**Decision:** see Q8 in the batch above.

#### Q9: Tumblr and Blogger blogs

Which blogs will wear the themes (their addresses), and what they publish
(text, pictures, both)? A theme is tried only by installing it on a blog,
which needs the account owner.

*Lean:* full minimal themes (Tumblr HTML with its blocks, Blogger XML), light
and dark from the visitor's scheme; the author installs them on a test blog
first.

**Decision:** see Q9 in the batch above.

#### Q10: the copyright holder

The notices say "© Sett Sarverott A.A.B. (RedScope Technologies)". Is
RedScope Technologies a registered business that should hold the rights
itself (its full legal name, registry number)?

*Lean:* keep the wording until the author names the entity.

**Decision:** see Q10 in the batch above.

### What was done with them

- Q4: the text font is a terminal-like monospace from the system's fonts
  (`--rs-font-text`), no font files. The logo and lettering will change
  soon, similar but not the same: the logo pipeline keeps no assumption
  beyond the masters and two crop constants in `scripts/build.py`.
- Q5: an npm package, split for Vue, React, Astro and vanilla web projects,
  goes to Later in TODO.
- Q6: option c): starters live here in `starters/`, template repositories
  once one is used for real.
- Q7: Read the Docs with Sphinx first (Furo theme); MkDocs later.
- Q8: GitBook gets the base customization: values and files to enter.
- Q9: Tumblr `redscope.tumblr.com` (images), Blogger `blog.redscope.online`
  (articles and news; origin `redscopetech.blogspot.com`).
- Q10: notices name RedScope Technologies (a business in preparation) as
  the holder and Sett Sarverott A.A.B. as the author, exercising the rights
  until the entity exists.
