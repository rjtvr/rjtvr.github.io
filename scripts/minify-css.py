"""Minify assets/site.css into assets/site.min.css (the file the pages load).

Usage:  python scripts/minify-css.py           write site.min.css
        python scripts/minify-css.py --check   exit 1 if site.min.css is stale

Conservative on purpose: it strips comments and whitespace but never rewrites
values or reorders rules, so the output behaves exactly like the source.
Quoted strings are kept verbatim, and spaces that CSS needs (descendant
selectors, `calc(a + b)`, `and` in media queries) are kept.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "assets" / "site.css"
TARGET = ROOT / "assets" / "site.min.css"


def minify(css: str) -> str:
    # One left-to-right pass: drop comments and park strings, so an apostrophe
    # inside a comment is never mistaken for a string (and vice versa).
    strings = []

    def comment_or_string(match):
        if match.group(0).startswith("/*"):
            return " "
        strings.append(match.group(0))
        return f"\0{len(strings) - 1}\0"

    css = re.sub(r'/\*.*?\*/|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'', comment_or_string, css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    # Whitespace never matters next to these characters.
    css = re.sub(r"\s*([{};,>])\s*", r"\1", css)
    # After a colon is safe; before one is not (".a :hover" differs from ".a:hover").
    css = re.sub(r":\s+", ":", css)
    css = css.replace(";}", "}")
    css = re.sub(r"\0(\d+)\0", lambda m: strings[int(m.group(1))], css)
    return css.strip() + "\n"


def main() -> int:
    output = minify(SOURCE.read_text(encoding="utf-8"))
    if "--check" in sys.argv:
        current = TARGET.read_text(encoding="utf-8") if TARGET.exists() else ""
        if current != output:
            print("assets/site.min.css is out of date: run python scripts/minify-css.py")
            return 1
        print("assets/site.min.css is in sync")
        return 0
    TARGET.write_text(output, encoding="utf-8", newline="\n")
    print(f"wrote {TARGET.relative_to(ROOT)} ({len(output)} bytes, source {SOURCE.stat().st_size})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
