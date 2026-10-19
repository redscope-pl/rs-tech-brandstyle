"""Build the style pack: src/ + resources/ -> dist/rs-tech-brandstyle/ and its tarball.

Usage: python scripts/build.py [--out DIR]   the pack
       python scripts/build.py resources     redraw the made images in resources/

- src/tokens.json becomes css/tokens.css: the palette (--rs-<family>-<shade>),
  --rs-light-*, --rs-dark-* always, and --rs-* following the visitor's scheme
  (or data-theme="light|dark" on <html>).
- Every app stylesheet under src/apps/ gets tokens.css put in front of it, so
  each output file stands alone (the apps can't load a shared file).
- resources/ holds the images (all rights reserved). Icons and the light/dark
  logos are made from the masters there and committed; tests/check.py fails
  when they are stale. Icons are cut from the source PNG (Pillow), not the SVG.
- starters/<name>/ are copied into starters/ of the pack with the brand put
  in: the pack's files into the folder STARTERS names, and the placeholders
  @@RS_TOKENS_CSS@@, @@RS_MARK_SVG@@, @@RS_VERSION@@ and
  @@RS_COLOR:<scheme>.<name>@@ (as #rrggbb) replaced in their text files.
- MANIFEST.sha256 lists every file; the tarball is reproducible (fixed mtime,
  owner and order), so a pinned release can be checked by its hash.
"""

import argparse
import gzip
import hashlib
import io
import json
import re
import shutil
import tarfile
import textwrap
import tomllib
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
RESOURCES = ROOT / "resources"
LOGO = RESOURCES / "images/logo"
NAME = "rs-tech-brandstyle"
# Square cut of the source logo around the eye (x, y, x + size, y + size).
MARK_BOX = (200, 100, 800, 700)
# First pixel row of the source logo below the eye (the words start there).
MARK_BOTTOM = 620
# Starters and where the pack's files go inside each (None: one-file themes,
# which take the brand through placeholders only).
STARTERS = {
    "sphinx": "_static/brand",
    "gitbook": "brand",
    "tumblr": None,
    "blogger": None,
    "vue": "public/brand",
    "react": "public/brand",
    "astro": "public/brand",
}
# What a starter gets of the pack, and what it never takes from its source.
STARTER_BRAND = ("css", "icons", "images", "NOTICE.md")
STARTER_SKIP = shutil.ignore_patterns("node_modules", "dist", "_build", ".astro", "brand")
TEXT = {".html", ".xml", ".css", ".py", ".md", ".rst", ".json", ".js", ".mjs", ".jsx", ".vue", ".astro", ".yaml", ".txt"}


def version() -> str:
    return tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]["version"]


def rgb(hex_color: str) -> str:
    return " ".join(str(int(hex_color[i : i + 2], 16)) for i in (1, 3, 5))


def color(ref: str) -> str:
    """A palette name ("night-900") as its #rrggbb."""
    family, shade = ref.rsplit("-", 1)
    return TOKENS["palette"][family][shade]


def tokens_css(tokens: dict) -> str:
    def block(selector: str, decls: list[str]) -> str:
        return selector + " {\n" + "".join(f"  {d}\n" for d in decls) + "}\n"

    fixed = []
    for family, shades in tokens["palette"].items():
        for shade, v in shades.items():
            fixed += [f"--rs-{family}-{shade}: {v};", f"--rs-{family}-{shade}-rgb: {rgb(v)};"]
    for scheme in ("light", "dark"):
        for k, ref in tokens[scheme].items():
            fixed += [f"--rs-{scheme}-{k}{s}: var(--rs-{ref}{s});" for s in ("", "-rgb")]
    fixed += [f"--rs-font-{k}: {v};" for k, v in tokens["font"].items() if not k.startswith("$")]
    fixed += [f"--rs-radius-{k}: {v};" for k, v in tokens["radius"].items()]

    def follow(scheme: str) -> list[str]:
        return [f"color-scheme: {scheme};"] + [
            f"--rs-{k}{s}: var(--rs-{scheme}-{k}{s});" for k in tokens[scheme] for s in ("", "-rgb")
        ]

    return (
        f"/* {NAME} {version()}: generated from src/tokens.json by scripts/build.py. */\n"
        + block(":root", fixed + follow("light"))
        + "@media (prefers-color-scheme: dark) {\n"
        + textwrap.indent(block(':root:not([data-theme="light"])', follow("dark")), "  ")
        + "}\n"
        + block(':root[data-theme="dark"]', follow("dark"))
    )


def with_tokens(css: str, tokens: str) -> str:
    """tokens.css in front of an app stylesheet; its @import lines stay first."""
    imports = re.findall(r"^@import [^\n]*\n", css, flags=re.M)
    rest = re.sub(r"^@import [^\n]*\n", "", css, flags=re.M)
    return "".join(imports) + tokens + "\n" + rest


def recolor(svg: str, color: str) -> str:
    return svg.replace('fill="#160100"', f'fill="{color}"')


def lockup(mark: str, words: str) -> str:
    """The eye above the words, as one SVG."""

    def inner(svg: str, x: int, y: int, w: int) -> str:
        box = re.search(r'viewBox="([^"]+)"', svg).group(1)
        bw, bh = (float(n) for n in box.split()[2:])
        body = re.sub(r"^<svg[^>]*>|</svg>\s*$|<title[^<]*</title>|<!--.*?-->", "", svg.strip(), flags=re.S)
        h = round(w * bh / bw)
        return f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="{box}">{body.strip()}</svg>', h

    m, mh = inner(mark, 130, 0, 340)
    t, th = inner(words, 0, mh + 40, 600)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 {mh + 40 + th}" role="img" aria-labelledby="t">\n'
        f'  <title id="t">RedScope Technologies</title>\n  {m}\n  {t}\n</svg>\n'
    )


def icons(out: Path) -> None:
    src = Image.open(LOGO / "redscope-tech-logo.source.png").convert("RGB")
    # The eye alone: alpha from how red a pixel is, the words below it left out.
    r, g, _ = src.split()
    alpha = Image.merge("RGB", (r, g, g)).convert("L", (1, -1, 0, 0))
    alpha = Image.eval(alpha, lambda v: max(0, min(255, (v - 40) * 3)))
    alpha.paste(0, (0, MARK_BOTTOM, src.width, src.height))
    def channels(ref: str) -> tuple[int, ...]:
        return tuple(int(c) for c in rgb(color(ref)).split())

    mark = Image.new("RGBA", src.size, channels("red-600") + (0,))
    mark.putalpha(alpha)
    mark = mark.crop(MARK_BOX)
    mark.resize((512, 512), Image.LANCZOS).save(out / "mark-512.png", optimize=True)
    # App icons and favicons: the eye on the night of the logo.
    icon = Image.new("RGBA", mark.size, channels("night-900") + (255,))
    icon.alpha_composite(mark)
    icon = icon.convert("RGB")
    for size in (180, 192, 512):
        icon.resize((size, size), Image.LANCZOS).save(out / f"icon-{size}.png", optimize=True)
    icon.resize((32, 32), Image.LANCZOS).save(out / "favicon-32.png", optimize=True)
    icon.save(out / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])


def render_resources(dest: Path) -> list[Path]:
    """The images made from the masters: dest/icons/, dest/images/logo/*-{light,dark}.svg."""
    (dest / "icons").mkdir(parents=True, exist_ok=True)
    (dest / "images/logo").mkdir(parents=True, exist_ok=True)
    icons(dest / "icons")
    mark = (LOGO / "mark.svg").read_text()
    words = (LOGO / "wordmark.svg").read_text()
    on_light, on_dark = color(TOKENS["light"]["fg"]), color(TOKENS["dark"]["fg"])
    logos = {
        "wordmark-light.svg": recolor(words, on_light),
        "wordmark-dark.svg": recolor(words, on_dark),
        "logo-light.svg": lockup(mark, recolor(words, on_light)),
        "logo-dark.svg": lockup(mark, recolor(words, on_dark)),
    }
    for name, svg in logos.items():
        (dest / "images/logo" / name).write_text(svg)
    return sorted([*(dest / "icons").iterdir(), *(dest / "images/logo" / n for n in logos)])


def placeholders(text: str, tokens: str) -> str:
    mark = re.sub(r"<!--.*?-->\s*", "", (LOGO / "mark.svg").read_text(), flags=re.S).strip()
    text = text.replace("@@RS_TOKENS_CSS@@", tokens).replace("@@RS_MARK_SVG@@", mark)
    text = text.replace("@@RS_VERSION@@", version())
    return re.sub(
        r"@@RS_COLOR:(light|dark)\.([a-z-]+)@@", lambda m: color(TOKENS[m.group(1)][m.group(2)]), text
    )


def starters(pack: Path, tokens: str) -> None:
    for name, brand_dir in STARTERS.items():
        target = pack / "starters" / name
        shutil.copytree(ROOT / "starters" / name, target, ignore=STARTER_SKIP)
        for f in sorted(target.rglob("*")):
            if f.is_file() and f.suffix in TEXT:
                f.write_text(placeholders(f.read_text(), tokens))
        if brand_dir:
            for part in STARTER_BRAND:
                src = pack / part
                if src.is_dir():
                    shutil.copytree(src, target / brand_dir / part)
                else:
                    shutil.copyfile(src, target / brand_dir / part)
    shutil.copyfile(ROOT / "starters/README.md", pack / "starters/README.md")


def build(out: Path) -> Path:
    pack = out / NAME
    shutil.rmtree(pack, ignore_errors=True)
    (pack / "css").mkdir(parents=True)

    tokens = tokens_css(TOKENS)
    (pack / "css/tokens.css").write_text(tokens)
    (pack / "css/zone.css").write_text(with_tokens((SRC / "css/zone.css").read_text(), tokens))

    # resources/ as it is (icons/, images/), with its notice; the legal notices
    # and the code's licence go along, so every copy carries them.
    shutil.copytree(RESOURCES, pack, dirs_exist_ok=True)
    shutil.copytree(ROOT / "docs/legal", pack / "legal")
    shutil.copyfile(ROOT / "LICENSE", pack / "LICENSE")

    # Per-app files keep their path under src/apps/; stylesheets get the tokens.
    for f in sorted((SRC / "apps").rglob("*")):
        if f.is_file():
            target = pack / f.relative_to(SRC / "apps")
            target.parent.mkdir(parents=True, exist_ok=True)
            if f.suffix == ".css" or f.name.endswith(".scss.hbs"):
                target.write_text(with_tokens(f.read_text(), tokens))
            else:
                shutil.copyfile(f, target)
    # Images each app expects under its own names (see docs/usage.md).
    gitea_img = pack / "gitea/public/assets/img"
    gitea_img.mkdir(parents=True, exist_ok=True)
    for src_name, name in [
        ("images/logo/mark.svg", "logo.svg"),
        ("icons/icon-512.png", "logo.png"),
        ("images/logo/mark.svg", "favicon.svg"),
        ("icons/favicon-32.png", "favicon.png"),
        ("icons/icon-180.png", "apple-touch-icon.png"),
    ]:
        shutil.copyfile(pack / src_name, gitea_img / name)
    shutil.copyfile(pack / "images/backgrounds/flow-background.svg", pack / "authentik/flow-background.svg")

    starters(pack, tokens)

    files = sorted(p for p in pack.rglob("*") if p.is_file())
    manifest = "".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(pack)}\n" for p in files)
    (pack / "MANIFEST.sha256").write_text(manifest)
    return tarball(out, pack)


def tarball(out: Path, pack: Path) -> Path:
    def norm(info: tarfile.TarInfo) -> tarfile.TarInfo:
        info.mtime, info.uid, info.gid, info.uname, info.gname = 0, 0, 0, "", ""
        info.mode = 0o755 if info.isdir() else 0o644
        return info

    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w", format=tarfile.PAX_FORMAT) as tar:
        for p in [pack, *sorted(pack.rglob("*"))]:
            tar.add(p, arcname=str(p.relative_to(out)), recursive=False, filter=norm)
    path = out / f"{NAME}-{version()}.tar.gz"
    with open(path, "wb") as f, gzip.GzipFile(filename="", mode="wb", fileobj=f, mtime=0) as gz:
        gz.write(buf.getvalue())
    return path


TOKENS = json.loads((SRC / "tokens.json").read_text())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("what", nargs="?", choices=["pack", "resources"], default="pack")
    parser.add_argument("--out", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    if args.what == "resources":
        for p in render_resources(RESOURCES):
            print(p.relative_to(ROOT))
    else:
        path = build(args.out.resolve())
        print(f"{path}  sha256 {hashlib.sha256(path.read_bytes()).hexdigest()}")
