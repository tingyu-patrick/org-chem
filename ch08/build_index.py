#!/usr/bin/env python3
"""Generate ch08/index.md (reagent -> reaction lookup + misconception stats) from cards/*.md and ../misconceptions.md."""

from collections import Counter
from pathlib import Path
import re
import yaml

BASE_DIR = Path(__file__).resolve().parent
CARDS_DIR = BASE_DIR / "cards"
INDEX_PATH = BASE_DIR / "index.md"
MISCONCEPTIONS_PATH = BASE_DIR.parent / "misconceptions.md"
MISCONCEPTIONS_REL_LINK = "../misconceptions.md"
MECHANISMS_REL_LINK = "../mechanisms.md"

MECHANISM_ANCHORS = {
    "hx-addition": "1-hx-addition",
    "x2-addition": "2-x2-addition",
    "halohydrin": "3-halohydrin",
    "oxymercuration": "4-oxymercuration",
    "hydroboration": "5-hydroboration",
    "hydrogenation": "6-hydrogenation",
    "epoxidation": "7-epoxidation",
    "epoxide-hydrolysis": "8-epoxide-hydrolysis",
    "oso4-hydroxylation": "9-oso4-hydroxylation",
    "carbene-dichloro": "10-carbene-dichloro",
    "simmons-smith": "11-simmons-smith",
    "ozonolysis": "12-ozonolysis",
    "kmno4-cleavage": "13-kmno4-cleavage",
    "diol-cleavage": "14-diol-cleavage",
}


def parse_frontmatter(md_path: Path) -> dict:
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"Missing YAML frontmatter in {md_path}")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"Unclosed YAML frontmatter in {md_path}")
    data = yaml.safe_load(parts[1])
    if not isinstance(data, dict):
        raise ValueError(f"Invalid YAML frontmatter in {md_path}")
    return data


def normalize_family(raw_family: str) -> str:
    lower = raw_family.lower()
    for label in ("syn", "anti", "cleavage", "cation"):
        if lower.startswith(label):
            return f"{label} ({raw_family})" if raw_family != label and not lower.startswith(f"{label} (") else raw_family
    if "three-membered-ring" in lower:
        return f"anti ({raw_family})"
    return raw_family


def parse_misconception_counts() -> tuple[int, Counter[str], Counter[tuple[str, str]]]:
    """Return (total_entries, slug_counter, (chapter, slug) counter) from ../misconceptions.md."""
    counts: Counter[str] = Counter()
    chap_slug_counts: Counter[tuple[str, str]] = Counter()
    if not MISCONCEPTIONS_PATH.exists():
        return 0, counts, chap_slug_counts

    raw = MISCONCEPTIONS_PATH.read_text(encoding="utf-8")
    cleaned = re.sub(r"<!--.*?-->", "", raw, flags=re.DOTALL)

    total = 0
    for line in cleaned.splitlines():
        line = line.strip()
        if not line.startswith("|") or not line.endswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 5:
            continue
        # Skip header and markdown separator rows
        if cells[0].startswith("章節") or all(set(c) <= {"-", ":"} for c in cells if c):
            continue
        if not any(cells):
            continue

        total += 1
        chapter_field = cells[0].replace("`", "").strip()
        slug_field = cells[1].replace("`", "").strip()
        for token in re.split(r"[,;/\s]+", slug_field):
            token = token.strip()
            if token:
                counts[token] += 1
                chap_slug_counts[(chapter_field, token)] += 1

    return total, counts, chap_slug_counts


def build_index() -> str:
    total_misc, misc_counts, chap_slug_counts = parse_misconception_counts()
    rows = []
    known_slugs = set()

    for md_path in sorted(CARDS_DIR.glob("*.md")):
        meta = parse_frontmatter(md_path)
        slug = meta["slug"]
        known_slugs.add(slug)
        name = meta["name"]
        reagents_list = meta["reagents"]
        if isinstance(reagents_list, list):
            reagent_str = "; ".join(str(r) for r in reagents_list)
        else:
            reagent_str = str(reagents_list)
        family_str = normalize_family(str(meta["family"]))
        reaction_link = f"[{name} (`{slug}`)](cards/{slug}.md)"
        mech_anchor = MECHANISM_ANCHORS.get(slug, "")
        mech_link = f"[詳解]({MECHANISMS_REL_LINK}#{mech_anchor})" if mech_anchor else f"[詳解]({MECHANISMS_REL_LINK})"
        note_count = misc_counts.get(slug, 0)
        note_cell = f"[{note_count} 則]({MISCONCEPTIONS_REL_LINK})" if note_count > 0 else "0"
        rows.append((reagent_str, reaction_link, family_str, mech_link, note_cell))

    rows.sort(key=lambda r: (r[0].lower(), r[1].lower()))

    other_items = [
        f"`{chap}:{slug}` ×{cnt}" if chap else f"`{slug}` ×{cnt}"
        for (chap, slug), cnt in sorted(chap_slug_counts.items())
        if slug not in known_slugs and cnt > 0
    ]
    other_summary = "；跨章節／其他：" + ", ".join(other_items) if other_items else ""

    lines = [
        "# Ch08 Alkenes: Reagent → Reaction Index",
        "",
        "> Generic principle: **syn** = concerted; **anti** = three-membered ring opened by back-side attack.",
        f"> ⚙️ **完整反應機構詳解（Mechanisms）**：[../mechanisms.md]({MECHANISMS_REL_LINK})",
        f"> 📒 **跨章節觀念迷思總表（原本以為 vs 其實是）**：[../misconceptions.md]({MISCONCEPTIONS_REL_LINK})（目前共紀錄 **{total_misc}** 則{other_summary}）",
        "",
        "| Reagent | Reaction | Family (syn / anti / cleavage / cation) | Mechanism | 迷思筆記 |",
        "|---|---|---|---|---|",
    ]
    for reagent, reaction, family, mech_link, note_cell in rows:
        lines.append(f"| `{reagent}` | {reaction} | {family} | {mech_link} | {note_cell} |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    content = build_index()
    INDEX_PATH.write_text(content, encoding="utf-8")
    print(f"Wrote {INDEX_PATH} with {len(list(CARDS_DIR.glob('*.md')))} reactions.")


if __name__ == "__main__":
    main()
