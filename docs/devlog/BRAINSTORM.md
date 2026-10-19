# BRAINSTORM

Open questions. Each has a *Lean:* (what an agent would do if told to pick)
and gets a **Decision:** from the author. Agents don't settle them in code.

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

## Q6: where the starting packets live

The vision asks for starting packets: GitBook, Read the Docs, GitHub Pages
(Vue, React, Astro), Tumblr, Blogger.

- a) here, `starters/<platform>/`, each minimal, built and checked with the pack
- b) one template repository per starter in the scope (GitHub "template
  repository"), each pulling a pinned pack release
- c) a) first, b) once a starter is used for real

*Lean:* c): one place to keep them in step while the pack changes fast.

## Q7: Read the Docs: which documentation tool

Read the Docs builds Sphinx and MkDocs (and others). Each needs its own theme.

- a) MkDocs with Material (an `extra.css` and the logo)
- b) Sphinx with Furo (CSS variables, light and dark)
- c) both

*Lean:* a): Markdown like the rest of our docs; Material has light/dark and
takes CSS variables.

## Q8: GitBook

Hosted GitBook takes the brand through its settings (primary colour, logo,
favicon, fonts from a list), not through CSS. The packet would be the values
and files to enter, and a guide.

*Lean:* that, unless there is a self-hosted GitBook (legacy CLI) in use.

## Q9: Tumblr and Blogger blogs

Which blogs will wear the themes (their addresses), and what they publish
(text, pictures, both)? A theme is tried only by installing it on a blog,
which needs the account owner.

*Lean:* full minimal themes (Tumblr HTML with its blocks, Blogger XML), light
and dark from the visitor's scheme; the author installs them on a test blog
first.

## Q10: the copyright holder

The notices say "© Sett Sarverott A.A.B. (RedScope Technologies)". Is
RedScope Technologies a registered business that should hold the rights
itself (its full legal name, registry number)?

*Lean:* keep the wording until the author names the entity.
