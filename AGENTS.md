# rs-tech-brandstyle — agent & contributor guide

The RedScope Technologies style pack. This file is for AI agents (Claude
Code, Codex, Gemini CLI, Copilot, Cursor, Aider…) and humans alike. Keep it
current when something changes.

It complements the workshop-wide `__WORKSHOP/AGENTS.md` (BOS rules). Where
they differ, this file wins for this repository.

## What this is

One source of the brand (`src/tokens.json`, `src/logo/`) built into a pack
of files that the zone's software takes as they are: CSS variables, logos and
icons, themes for Authentik, Gitea, Vaultwarden and the zone's own pages. Its
first consumer is `forge/redscope-pl/rs-tech-infra` (its TODO Phase 8), which
pins a release tarball by version and hash.

Read first:

1. [docs/devlog/TODO.md](docs/devlog/TODO.md): what is being worked on now
2. [docs/devlog/BRAINSTORM.md](docs/devlog/BRAINSTORM.md): open questions `Q<n>`
3. [docs/usage.md](docs/usage.md): how each app takes its part of the pack

## Tooling and checks

```sh
uv sync                  # tools from PyPI: task, commitizen, lefthook, yamllint, Pillow
uv run task setup        # + lefthook git hooks
uv run task build        # dist/rs-tech-brandstyle/ + reproducible tarball
uv run task check        # tokens, contrast, SVGs, two builds compared, YAML, commits (= CI)
uv run task preview      # build, then open docs/preview.html
```

- **Gate every commit** on `uv run task check` (exit code, output to
  `/dev/null`).
- **Look at what you change.** `docs/preview.html?theme=light|dark` shows
  the built pack; headless Chromium can screenshot it.
- **Commits:** conventional commits, checked by commitizen in the lefthook
  `commit-msg` hook and in `task check`. Commits up to `7ce277f` predate it.
- **`.gitignore` is the generic template** with broad rules (`dist`, `lib/`,
  `build/`, `*.spec`…). If a new file doesn't show in `git status`, check
  `git check-ignore -v <file>`.

## Layout

```
src/tokens.json        colours (brand, light, dark), fonts, radii, contrast pairs
src/logo/              mark.svg, wordmark.svg (traced), the source PNGs
src/css/zone.css       base style of the zone's own pages
src/apps/<app>/        per-app files, laid out as the app expects them
scripts/build.py       src/ -> dist/ (tokens into every stylesheet, icons, manifest, tarball)
tests/check.py         the pack's checks
docs/                  usage, preview page; docs/devlog/ for plan and questions
docs/.agents/          agent notes (see below)
.github/workflows/     check (= task check), release (tags v*), CodeQL, issue summaries
```

## Rules for agents

1. **Follow the plan.** Work on the next unchecked item in TODO.md, or what
   the user asks. Tick it off when done and verified. Work that belongs to
   another repository is not done here: write it into
   `~/__WORKSHOP/forge/NOTES-for-repositories.md`.
2. **Don't settle open questions in code.** If a change depends on a `Q<n>`,
   ask, or pick the *Lean:* option only when told to.
3. **Colours live in `src/tokens.json` only.** App themes use `var(--rs-*)`;
   the check fails on a variable that tokens don't define, and on contrast
   below WCAG AA.
4. **No outside resources** in the pack (fonts, images, CSS from other
   hosts): the zone's pages load nothing from third parties.
5. **Don't edit `dist/`** or the source PNGs; build from `src/`.
6. **Say what is untested.** A theme counts as working only after it was
   seen on the running app; keep the status lines in `docs/usage.md` true.
7. **Ask first** before anything outward-facing: pushing, tagging a
   release, publishing a package.
8. **Branches:** BOS flow `master` → `development` → … → `master` via PR.
   Work on `development`. On GitHub the default branch is still `main`, and
   the remote's development branch is spelled `developement`; the author
   decides how to reconcile them.
9. **Commits:** one per finished step, conventional message ending in the
   agent's `Co-Authored-By:` line. Pushing needs the author's go-ahead.

## `docs/.agents/` — agent notes

The author reads this directory **read-only**:

- `docs/.agents/NOTES.md`: findings, decisions taken with the user. Newest
  on top, dated.
- `docs/.agents/sources/`: snapshots of removed material (the template's
  README and package files), for reference, not a spec.

## BOS context

- This repo: `__WORKSHOP/forge/redscope-pl/rs-tech-brandstyle` (scope `redscope-pl`).
- Glossary of BOS terms: `__WORKSHOP/forge/blacksmith-organization-system/bos-skillset/docs/glossary/`.
- Loose notes of the author go to `__WORKSHOP/craftbook/scrapnotes/`, not here.
