"""Build every starter that can be built off its platform, from a fresh pack.

Usage: python tests/starters.py   (needs npm; downloads the starters' npm
packages into a scratch dir; exit code 1 on any failure)

Sphinx builds with warnings as errors; Vue, React and Astro run `npm ci` and
`npm run build`, then the built page must link the brand's stylesheet and
the brand files must be in the output.
"""

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import build  # noqa: E402

failures: list[str] = []


def run(name: str, cmd: list[str], cwd: Path) -> bool:
    done = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if done.returncode:
        failures.append(f"{name}: `{' '.join(cmd)}` exited {done.returncode}\n{done.stdout[-2000:]}{done.stderr[-2000:]}")
    return done.returncode == 0


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        build.build(Path(tmp))
        starters = Path(tmp) / build.NAME / "starters"

        sphinx = starters / "sphinx"
        if run("sphinx", [sys.executable, "-m", "sphinx", "-W", "-q", "-b", "html", ".", "_build/html"], sphinx):
            page = (sphinx / "_build/html/index.html").read_text()
            if "brand/css/tokens.css" not in page or "logo-light.svg" not in page:
                failures.append("sphinx: the page doesn't load the brand's tokens or logo")

        for name in ("vue", "react", "astro"):
            site = starters / name
            if run(name, ["npm", "ci", "--no-audit", "--no-fund"], site) and run(name, ["npm", "run", "build"], site):
                if "brand/css/zone.css" not in (site / "dist/index.html").read_text():
                    failures.append(f"{name}: dist/index.html doesn't link brand/css/zone.css")
                if not (site / "dist/brand/icons/favicon.ico").exists():
                    failures.append(f"{name}: dist/ has no brand files")

    for f in failures:
        print(f"FAIL {f}")
    print(f"{len(failures)} failure(s)" if failures else "starters: all built")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
