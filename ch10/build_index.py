#!/usr/bin/env python3
"""Generate ch10/index.md (reagent -> reaction lookup) from cards/*.md frontmatter."""

from pathlib import Path
import yaml

BASE_DIR = Path(__file__).resolve().parent
CARDS_DIR = BASE_DIR / "cards"
INDEX_PATH = BASE_DIR / "index.md"


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
    for label in ("radical", "cation", "substitution", "organometallic", "coupling"):
        if lower.startswith(label):
            return f"{label} ({raw_family})" if raw_family != label and not lower.startswith(f"{label} (") else raw_family
    return raw_family


def build_index() -> str:
    rows = []
    for md_path in sorted(CARDS_DIR.glob("*.md")):
        meta = parse_frontmatter(md_path)
        slug = meta["slug"]
        name = meta["name"]
        reagents_list = meta["reagents"]
        if isinstance(reagents_list, list):
            reagent_str = "; ".join(str(r) for r in reagents_list)
        else:
            reagent_str = str(reagents_list)
        family_str = normalize_family(str(meta["family"]))
        reaction_link = f"[{name} (`{slug}`)](cards/{slug}.md)"
        rows.append((reagent_str, reaction_link, family_str))

    rows.sort(key=lambda r: (r[0].lower(), r[1].lower()))

    lines = [
        "# Ch10 Organohalides: Reagent → Reaction Index",
        "",
        "> Core themes: **Radical stability** (`allylic ≈ benzylic > 3° > 2° > 1° > vinylic`); **Alcohol → Halide choice** (`3° ROH + HX` via SN1 vs `1°/2° ROH + SOCl2 or PBr3` via SN2 inversion without rearrangement); **Organometallics & Coupling** (`RMgX` = strong base/nucleophile, destroyed by protic groups; `R2CuLi` = Gilman coupling with `R'–X`; `Suzuki–Miyaura` = `Pd`-catalyzed `R–B(OH)2 + R'–X` coupling).",
        "",
        "| Reagent | Reaction | Family (radical / cation / substitution / organometallic / coupling) |",
        "|---|---|---|",
    ]
    for reagent, reaction, family in rows:
        lines.append(f"| `{reagent}` | {reaction} | {family} |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    content = build_index()
    INDEX_PATH.write_text(content, encoding="utf-8")
    print(f"Wrote {INDEX_PATH} with {len(list(CARDS_DIR.glob('*.md')))} reactions.")


if __name__ == "__main__":
    main()
