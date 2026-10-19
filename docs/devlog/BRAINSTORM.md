# BRAINSTORM

Open questions. Each has a *Lean:* (what an agent would do if told to pick)
and gets a **Decision:** from the author. Agents don't settle them in code.


## Q11: what "accessible data reading" means

The third orders: "prepare this to handle accessible data reading". Read as
both: (1) the pack reads public data (gitrecon's output in
`redscope-pl/.github`) into pages, `js/rs-data.js`; (2) what it shows stays
accessible (screen readers, keyboard, contrast, reduced motion).

*Lean:* both, as built; correct me if one of them was meant only.

## Q12: where the gathered data lives, and its shape

gitrecon (run by rs-tech-infra) gathers static data into `redscope-pl/.github`
(public) and `redscope-pl/.github-private`. `.github-private` is the org's
members-only profile repository: its files are not readable by the public or
by a page's script without a token.

- a) `.github/data/<source>.json` (public) plus `data/index.json` listing
  them, each file an array of records as GitHub gives them; private data
  only in `.github-private`, never read by public pages
- b) the same, but the sites read the data at their build (GitHub Actions),
  not in the visitor's browser

*Lean:* a) for now (`rs-data.js` reads it live from
`raw.githubusercontent.com`), b) once there is a lot of data.

## Q13: the 3D background of the drafts

The drafts draw a turning wireframe icosahedron with three.js from a CDN.
The pack loads nothing from outside, and three.js is ~600 KB.

*Lean:* later, as an opt-in script of the npm packages (Q5), off under
reduced motion; not in the Blogger theme.

## Q14: removing the Blogger drafts

The orders say to remove `starters/blogger/draft-theme.xml` and
`draft-homepage/` once taken into the pack (done). They are untracked: the
agent's attempt to commit them first (to keep them in git history) was
refused by its permission system, and deleting them unsaved would lose them.

- a) the author deletes them (has copies elsewhere, e.g. AI Studio)
- b) moved to `__WORKSHOP/craftbook/scrapnotes/` (BOS: drafts of the author)
- c) the author commits them once, then an agent removes them

*Lean:* b).
