#!/usr/bin/env python3
"""Build OrbitKit dist files.

Inlines src/orbitkit.css @imports into dist/orbitkit.css and
produces a minified dist/orbitkit.min.css. No dependencies.
Usage: python3 scripts/build.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "orbitkit.css"
DIST = ROOT / "dist"
ORDER = [
    "_base.css", "orbit.css", "ring.css", "dual-ring.css", "pulse-ring.css",
    "comet.css", "bars.css", "dots.css", "typing.css", "grid.css",
    "morph.css", "flip.css", "progress.css",
]

HEADER = """/* ============================================================
   OrbitKit v%s — https://github.com/karma1911/orbitkit
   A collection of loading indicators animated with CSS.
   MIT License.
   ============================================================ */
"""


def version() -> str:
    import json
    return json.loads((ROOT / "package.json").read_text())["version"]


def minify(css: str) -> str:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)   # strip comments
    css = re.sub(r"\s+", " ", css)                    # collapse whitespace
    css = re.sub(r"\s*([{}:;,>+~])\s*", r"\1", css)   # tighten punctuation
    css = re.sub(r";}", "}", css)
    return css.strip()


def main() -> None:
    DIST.mkdir(exist_ok=True)
    parts = []
    for name in ORDER:
        css = (ROOT / "src" / "spinners" / name).read_text()
        parts.append(css.strip())
    bundled = HEADER % version() + "\n\n".join(parts) + "\n"
    (DIST / "orbitkit.css").write_text(bundled)
    (DIST / "orbitkit.min.css").write_text(minify(bundled) + "\n")
    print(f"wrote dist/orbitkit.css ({len(bundled)} bytes)")
    print(f"wrote dist/orbitkit.min.css ({len(minify(bundled))} bytes)")


if __name__ == "__main__":
    main()
