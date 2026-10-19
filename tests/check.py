"""Static checks of the style pack: tokens, contrast, SVGs, resources, the built pack.

Usage: python tests/check.py   (exit code 1 on any failure, every failure listed)
"""

import hashlib
import json
import re
import sys
import tarfile
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import build  # noqa: E402

HEX = re.compile(r"^#[0-9a-f]{6}$")
failures: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def luminance(hex_color: str) -> float:
    def lin(c: float) -> float:
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (lin(int(hex_color[i : i + 2], 16) / 255) for i in (1, 3, 5))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a: str, b: str) -> float:
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def check_tokens(tokens: dict) -> None:
    for family, shades in tokens["palette"].items():
        for shade, v in shades.items():
            if not HEX.match(v):
                fail(f"tokens.json palette.{family}.{shade}: {v!r} is not #rrggbb (lower case)")
    if tokens["light"].keys() != tokens["dark"].keys():
        fail("tokens.json: light and dark have different names")
    for scheme in ("light", "dark"):
        for k, ref in tokens[scheme].items():
            try:
                build.color(ref)
            except (KeyError, ValueError):
                fail(f"tokens.json {scheme}.{k}: {ref!r} is not a palette shade")
                return
    for scheme in ("light", "dark"):
        for fg, bg in tokens["contrast"]["pairs"]:
            ratio = contrast(build.color(tokens[scheme][fg]), build.color(tokens[scheme][bg]))
            if ratio < 4.5:
                fail(f"contrast {scheme} {fg} on {bg}: {ratio:.2f} < 4.5 (WCAG AA)")


def check_svgs() -> None:
    for svg in sorted([*(ROOT / "src").rglob("*.svg"), *(ROOT / "resources").rglob("*.svg")]):
        try:
            root = ET.parse(svg).getroot()
        except ET.ParseError as e:
            fail(f"{svg.relative_to(ROOT)}: {e}")
            continue
        if not root.get("viewBox"):
            fail(f"{svg.relative_to(ROOT)}: no viewBox")
        if re.search(r"(href|url)\(?\s*=?\s*[\"']?https?:", svg.read_text()):
            fail(f"{svg.relative_to(ROOT)}: loads an outside resource")


def check_resources(out: Path) -> None:
    for made in build.render_resources(out):
        committed = build.RESOURCES / made.relative_to(out)
        if not committed.exists() or committed.read_bytes() != made.read_bytes():
            fail(f"resources/{made.relative_to(out)} is stale: run `task resources` and commit")


def check_pack(out: Path, tokens: dict) -> None:
    first = build.build(out / "a")
    second = build.build(out / "b")
    if first.read_bytes() != second.read_bytes():
        fail("build: two builds gave different tarballs (not reproducible)")
    pack = out / "a" / build.NAME

    defined = set(re.findall(r"(--rs-[a-z0-9-]+):", (pack / "css/tokens.css").read_text()))
    for css in sorted(pack.rglob("*")):
        if css.suffix == ".css" or css.name.endswith(".scss.hbs"):
            text = css.read_text()
            for name in sorted(set(re.findall(r"var\((--rs-[a-z0-9-]+)\)", text)) - defined):
                fail(f"{css.relative_to(pack)}: var({name}) is not defined by tokens.json")
            if re.search(r"url\(\s*[\"']?https?:|@import\s+[\"']?(url\()?\s*[\"']?https?:", text):
                fail(f"{css.relative_to(pack)}: loads an outside resource")
            bare = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
            if "{" in bare and "@import" in bare[bare.index("{") :]:
                fail(f"{css.relative_to(pack)}: @import after a rule (browsers ignore it)")

    listed = {}
    for line in (pack / "MANIFEST.sha256").read_text().splitlines():
        digest, path = line.split("  ", 1)
        listed[path] = digest
    for path, digest in listed.items():
        if hashlib.sha256((pack / path).read_bytes()).hexdigest() != digest:
            fail(f"MANIFEST.sha256: {path} does not match")
    on_disk = {str(p.relative_to(pack)) for p in pack.rglob("*") if p.is_file()} - {"MANIFEST.sha256"}
    if on_disk != set(listed):
        fail(f"MANIFEST.sha256: lists {sorted(set(listed) ^ on_disk)} wrongly")

    with tarfile.open(first) as tar:
        names = tar.getnames()
    if any(not n.startswith(build.NAME) for n in names):
        fail("tarball: entries outside rs-tech-brandstyle/")


def main() -> int:
    tokens = json.loads((ROOT / "src/tokens.json").read_text())
    check_tokens(tokens)
    check_svgs()
    with tempfile.TemporaryDirectory() as tmp:
        check_resources(Path(tmp) / "resources")
        check_pack(Path(tmp), tokens)
    for f in failures:
        print(f"FAIL {f}")
    print(f"{len(failures)} failure(s)" if failures else "check: all passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
