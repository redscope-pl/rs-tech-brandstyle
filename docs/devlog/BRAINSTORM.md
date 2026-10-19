# BRAINSTORM

Open questions. Each has a *Lean:* (what an agent would do if told to pick)
and gets a **Decision:** from the author. Agents don't settle them in code.

## Q1: the licence

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

## Q2: colours

Sampled from the logo: red `#b11020` on night `#160100`. Light scheme:
warm white `#fbf8f6`, links and buttons in the logo red. Dark scheme: the
logo's night as background, a lighter red `#f2444f` for links (the logo red
on night is too dark for text, 2.5:1).

*Lean:* keep them until the author corrects.

## Q3: the logo as vectors

The eye and the words in `src/logo/` are traced from the PNGs of the site
(1000 px logo, 809 px words). The eye is close; the words are smoothed from
a small, noisy PNG. Is there an original vector file (the designer's)?

*Lean:* use the traced ones until an original turns up; replace then.

## Q4: a brand font

The words of the logo are lettering (a cut R, T, E), not a font the pages
can use. Pages use the system font now.

- a) system fonts (no files, nothing to load)
- b) a self-hosted open font close to the lettering (OFL)

*Lean:* a) until there is a reason.

## Q5: npm package

The old `package.json` named the pack for npm. Publishing to npm is outward
and permanent.

*Lean:* not now; the tarball release is enough for the zone.
