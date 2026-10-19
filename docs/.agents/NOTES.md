# Agent notes

Running notes of agents: findings, decisions taken with the user. Newest on
top, dated. The author reads this read-only.

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
