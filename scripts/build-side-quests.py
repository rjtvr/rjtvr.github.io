"""Render the Workshop's Side quests cards from data/side-quests.json.

Usage:  python scripts/build-side-quests.py           rewrite the cards in workshop.html
        python scripts/build-side-quests.py --check   exit 1 if workshop.html is stale

Only the lines between the side-quests:start and side-quests:end comments in
workshop.html are replaced; everything else in the page is left untouched.
All text from the JSON is HTML-escaped. Python 3, no dependencies.
"""

import json
import re
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "side-quests.json"
PAGE = ROOT / "workshop.html"

START = "<!-- side-quests:start (generated from data/side-quests.json; run python scripts/build-side-quests.py) -->"
END = "<!-- side-quests:end -->"
INDENT = " " * 10  # Cards sit inside .row.quest-cards.
REQUIRED = ("id", "name", "language", "status", "summary")


def validate(quests) -> list:
    errors, seen = [], set()
    if not isinstance(quests, list) or not quests:
        return ['"quests" must be a non-empty list']
    for n, quest in enumerate(quests, 1):
        where = f"quest {n} ({quest.get('name', '?')})" if isinstance(quest, dict) else f"quest {n}"
        if not isinstance(quest, dict):
            errors.append(f"{where}: must be an object")
            continue
        for key in REQUIRED:
            if not isinstance(quest.get(key), str) or not quest[key].strip():
                errors.append(f'{where}: "{key}" must be a non-empty string')
        qid = quest.get("id", "")
        if isinstance(qid, str) and not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", qid):
            errors.append(f'{where}: "id" must be lowercase and hyphenated, like "dot-snake"')
        if qid in seen:
            errors.append(f'{where}: duplicate id "{qid}"')
        seen.add(qid)
        repo = quest.get("repo")
        if repo is not None and not (isinstance(repo, str) and repo.startswith("https://")):
            errors.append(f'{where}: "repo" must be an https:// URL or null')
        chips = quest.get("chips", [])
        if not isinstance(chips, list) or any(
            not isinstance(c, dict) or not isinstance(c.get("label"), str) or not c["label"].strip()
            for c in chips
        ):
            errors.append(f'{where}: "chips" must be a list of {{"label": "..."}} objects')
    return errors


def text(value: str) -> str:
    """Escape element text; quotes only need escaping inside attributes."""
    return escape(value, quote=False)


def render_card(quest: dict) -> str:
    chips = "\n".join(
        f'    <span class="badge chip small{" be" if chip.get("backend") else ""}">{text(chip["label"])}</span>'
        for chip in quest.get("chips", [])
    )
    if quest.get("repo"):
        link = f'  <a href="{escape(quest["repo"])}" class="quest-link" rel="noopener">View on GitHub →</a>'
    else:
        link = '  <span class="quest-link soon">Repo coming soon</span>'
    lines = [
        f'<article id="{escape(quest["id"])}" class="col-4 quest-card">',
        '  <div class="hstack justify-between gap-2">',
        f'    <span class="quest-lang">{text(quest["language"])}</span>',
        f'    <span class="quest-status">{text(quest["status"])}</span>',
        "  </div>",
        f'  <h3>{text(quest["name"])}</h3>',
        f'  <p>{text(quest["summary"])}</p>',
    ]
    if chips:
        lines += ['  <div class="hstack chips small">', chips, "  </div>"]
    lines += [link, "</article>"]
    return "\n".join(INDENT + line if line else line for line in "\n".join(lines).split("\n"))


def build(page: str, quests: list) -> str:
    newline = "\r\n" if "\r\n" in page else "\n"
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if len(pattern.findall(page)) != 1:
        raise SystemExit("workshop.html needs exactly one side-quests:start / side-quests:end marker pair")
    cards = "\n\n".join(render_card(q) for q in quests)
    block = f"{START}\n\n{cards}\n\n{INDENT}{END}".replace("\n", newline)
    return pattern.sub(lambda _: block, page)


def main() -> int:
    try:
        data = json.loads(DATA.read_text(encoding="utf-8"))
    except json.JSONDecodeError as err:
        print(f"data/side-quests.json is not valid JSON: {err}")
        return 1
    quests = data.get("quests") if isinstance(data, dict) else None
    errors = validate(quests)
    if errors:
        print("data/side-quests.json has problems:\n  " + "\n  ".join(errors))
        return 1
    page = PAGE.read_bytes().decode("utf-8")
    output = build(page, quests)
    if "--check" in sys.argv:
        if output != page:
            print("workshop.html is out of date: run python scripts/build-side-quests.py")
            return 1
        print("workshop.html side quests are in sync")
        return 0
    PAGE.write_bytes(output.encode("utf-8"))
    print(f"wrote {len(quests)} side quests into workshop.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
