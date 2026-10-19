# Agent notes

Running notes of agents: findings, decisions taken with the user. Newest on
top, dated. The author reads this read-only.

## 2026-10-19 (later) · UNIXUSAT=1792440094683

- First batch of ORDERS answered Q1–Q3 and gave a vision draft; archived
  in `docs/changelog/phase-1.md` (orders quoted, question headings demoted
  to fit the page; wording unchanged).
- Q2 read as: the palette is only night, gray, white, red, crimson (the old
  warm white `#fbf8f6` became `gray-50`, text in light mode is `night-900`).
  Crimson got a role, `highlight`; nothing uses it yet besides the preview.
- Q3 read as: `resources/icons/`, `resources/images/`, `resources/media/`
  (not created while empty). Made images are committed there, since the
  author wants icons in `resources/`; `task check` renders them again and
  compares bytes (depends on the Pillow pinned in `uv.lock`).
- "Universal documents" read as notices written to be reused by any project
  (`docs/legal/`), shipped inside the pack as `legal/`. The trademark notice
  claims no registration (unknown); Q10 asks about the legal entity.
- New questions Q6–Q10 for the vision's starting packets.

## 2026-10-19 · UNIXUSAT=1792438233635

- Rewrite from the template on branch `development` (local; the remote
  branch is spelled `developement`). Old README, `package.json`,
  `composer.json`, `pyproject.toml` kept in `sources/`; the Docker
  hello-world files dropped (in git history).
- Brand colours sampled from `redscope.pl/src/assets/redscope-tech-logo.png`
  (red `#b11020`, night `#160100`). Logos traced with potracer
  (pure-Python potrace) through `uvx`; the trace scripts are not in the repo
  (one-off). The eye matches the PNG when overlaid; the words are smoothed.
- Raster icons come from the source PNG through Pillow, not from the SVG:
  no SVG renderer in CI. Headless Chromium (Playwright's
  `chrome-headless-shell`) works on this machine for looking at
  `docs/preview.html`; snap's chromium can't read the scratch dir.
- `issues-summary.yml` put the AI's answer into a shell command inside
  single quotes (an issue author could run commands); now through `$RESPONSE`.
  `codeql.yml` had an empty language matrix; now actions + python.
- App themes (Authentik, Gitea, Vaultwarden) use variable names from
  memory of those apps' CSS, not checked against the running versions.
  Guesses until Phase 2 tries them.
