#!/usr/bin/env python3
"""Convert ch10/cards/*.md into an Anki deck (ch10_organohalides.apkg) and CSV (ch10_organohalides.csv)."""

from __future__ import annotations

import csv
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
import genanki
import yaml

BASE_DIR = Path(__file__).resolve().parent
CARDS_DIR = BASE_DIR / "cards"
APKG_PATH = BASE_DIR / "ch10_organohalides.apkg"
CSV_PATH = BASE_DIR / "ch10_organohalides.csv"

DECK_NAME = "OrgChem::Ch10 Organohalides"
DECK_ID = 1849208110
MODEL_ID = 1607392821

CARD_CSS = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans TC", sans-serif;
  font-size: 18px;
  line-height: 1.5;
  color: #1f2937;
  background-color: #ffffff;
  padding: 16px;
}
.back {
  font-weight: 600;
  color: #111827;
  margin-bottom: 10px;
}
.why {
  margin-top: 10px;
  padding: 8px 12px;
  border-left: 3px solid #3b82f6;
  background-color: #f3f4f6;
  font-size: 15px;
  color: #374151;
}
.tags {
  margin-top: 12px;
  font-size: 12px;
  color: #6b7280;
}
details {
  margin-top: 6px;
  font-size: 14px;
}
"""

ANKI_MODEL = genanki.Model(
    MODEL_ID,
    "OrgChem Ch10 Reaction Model",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
        {"name": "Why"},
        {"name": "Tags"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "<div class='front'>{{Front}}</div>",
            "afmt": (
                "{{FrontSide}}<hr id='answer'>"
                "<div class='back'>{{Back}}</div>"
                "{{#Why}}<div class='why'><b>Why:</b> {{Why}}</div>{{/Why}}"
                "{{#Tags}}<div class='tags'>Tags: {{Tags}}</div>{{/Tags}}"
            ),
        }
    ],
    css=CARD_CSS,
)


@dataclass
class ReactionCard:
    slug: str
    name: str
    reagents: list[str]
    family: str
    tags: list[str]
    sections: dict[str, str]
    raw_text: str


@dataclass
class AnkiNoteSpec:
    guid: str
    slug: str
    card_type: str
    front: str
    back: str
    why: str
    tags: list[str]


def stable_guid(slug: str, card_type: str, extra: str = "") -> str:
    key = f"ch10::{slug}::{card_type}" if not extra else f"ch10::{slug}::{card_type}::{extra}"
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()[:10]
    return genanki.guid_for(digest)


def strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL).strip()


def clean_bullet(text: str) -> str:
    lines = []
    for line in strip_comments(text).splitlines():
        line = line.strip()
        if line.startswith("- "):
            line = line[2:].strip()
        if line:
            lines.append(line)
    return " | ".join(lines)


def parse_card(md_path: Path) -> ReactionCard:
    raw = md_path.read_text(encoding="utf-8")
    parts = raw.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"Invalid frontmatter in {md_path}")
    meta = yaml.safe_load(parts[1])
    body = parts[2]

    sections: dict[str, str] = {}
    current_header = None
    buffer: list[str] = []
    for line in body.splitlines():
        if line.startswith("## "):
            if current_header is not None:
                sections[current_header] = "\n".join(buffer).strip()
            current_header = line[3:].strip()
            buffer = []
        else:
            buffer.append(line)
    if current_header is not None:
        sections[current_header] = "\n".join(buffer).strip()

    return ReactionCard(
        slug=meta["slug"],
        name=meta["name"],
        reagents=list(meta["reagents"]),
        family=str(meta["family"]),
        tags=list(meta.get("tags", [])),
        sections=sections,
        raw_text=raw,
    )


STEREO_SLUGS = {
    "alkane-halogenation",
    "alcohol-hx",
    "alcohol-socl2",
    "alcohol-pbr3",
    "suzuki-coupling",
}

REARRANGEMENT_SLUGS = {
    "allylic-bromination",
    "alcohol-hx",
    "alcohol-socl2",
    "alcohol-pbr3",
}

CONTRAST_PROMPTS = {
    "alkane-halogenation": "對比：自由基鹵化中 `Cl2, hν` vs `Br2, hν` 的區域選擇性差異？",
    "allylic-bromination": "對比：烯類加 `NBS, hν, CCl4` vs `Br2, CH2Cl2` 的反應差異與原因？",
    "alcohol-hx": "對比：將醇轉為鹵代烷時，`HX` vs `SOCl2 / PBr3` 適用受質（1°/2°/3°）與重排差異？",
    "grignard-formation": "對比：製備 Grignard 試劑 (`RMgX`) 時，為什麼分子內不能有 `-OH`、`-NH2` 或 `-COOH`？且哪種鹵素不反應？",
    "gilman-coupling": "對比：`Gilman coupling` (`R2CuLi + R'–X`) vs `Grignard reagent` (`RMgX`) 的偶聯能力與受質限制？",
    "suzuki-coupling": "對比：`Suzuki–Miyaura coupling` 的催化循環三步驟為何？與 `Gilman` 相比有何官能基耐受優勢？",
}

PREDICTION_META = {
    ("alkane-halogenation", "(S)-3-methylhexane + Br2, hν → (±)-3-bromo-3-methylhexane (optically inactive racemic mixture)"): (
        "Planar achiral 3° radical intermediate is brominated with equal probability from both faces",
        "CCC(C)(Br)CCC",
    ),
    ("allylic-bromination", "cyclohexene + NBS, hν, CCl4 → 3-bromocyclohexene (single product because allylic radical is symmetrical)"): (
        "Allylic H abstraction gives symmetrical cyclohexenyl radical → single allylic bromide",
        "BrC1CCCC=C1",
    ),
    ("allylic-bromination", "1-butene + NBS, hν, CCl4 → mixture of 3-bromo-1-butene and 1-bromo-2-butene (via unsymmetrical allylic radical)"): (
        "Unsymmetrical allylic radical reacts at both C1 and C3 resonance positions",
        "CC(Br)C=C",
    ),
    ("allylic-bromination", "toluene + NBS, hν, CCl4 → (bromomethyl)benzene (benzyl bromide)"): (
        "Selective benzylic C–H abstraction forms resonance-stabilized benzyl radical",
        "BrCc1ccccc1",
    ),
    ("alcohol-hx", "1-methylcyclopentanol + HBr, ether → 1-bromo-1-methylcyclopentane"): (
        "3° alcohol reacts rapidly with HBr via tertiary carbocation (SN1)",
        "CC1(Br)CCCC1",
    ),
    ("alcohol-socl2", "(R)-2-butanol + SOCl2, pyridine → (S)-2-chlorobutane (inversion of configuration)"): (
        "SOCl2 in pyridine converts 2° OH into chlorosulfite leaving group followed by SN2 backside attack by Cl⁻",
        "CC[C@@H](C)Cl",
    ),
    ("alcohol-pbr3", "(S)-2-pentanol + PBr3, ether → (R)-2-bromopentane (inversion of configuration)"): (
        "PBr3 converts 2° OH into -OPBr2 leaving group followed by SN2 backside attack by Br⁻",
        "CCC[C@H](C)Br",
    ),
    ("grignard-formation", "2-bromobutane + 1. Mg, ether; 2. H2O → butane (overall reduction of R–Br to R–H)"): (
        "Mg forms sec-butylmagnesium bromide, which is protonated by water to give butane",
        "CCCC",
    ),
    ("gilman-coupling", "1-bromobutane + (CH3)2CuLi, ether → pentane + CH3Cu + LiBr"): (
        "Gilman reagent couples one methyl group with 1-bromobutane to extend the chain by 1 carbon",
        "CCCCC",
    ),
    ("suzuki-coupling", "phenylboronic acid + iodobenzene + Pd(PPh3)4, CaCO3, THF → biphenyl"): (
        "Pd(0)-catalyzed oxidative addition, transmetallation, and reductive elimination couple the two aryl rings",
        "c1ccc(-c2ccccc2)cc1",
    ),
}


def generate_notes(cards: list[ReactionCard]) -> list[AnkiNoteSpec]:
    notes: list[AnkiNoteSpec] = []
    seen_examples: set[str] = set()

    for card in cards:
        reagent_str = clean_bullet(card.sections.get("試劑", "; ".join(card.reagents)))
        interm_str = clean_bullet(card.sections.get("中間體", ""))
        regio_str = clean_bullet(card.sections.get("Regio", ""))
        stereo_str = clean_bullet(card.sections.get("Stereo", ""))
        rearr_str = clean_bullet(card.sections.get("Rearrangement", ""))
        contrast_str = clean_bullet(card.sections.get("對比", ""))
        pitfall_raw = strip_comments(card.sections.get("易錯", ""))
        examples_raw = strip_comments(card.sections.get("例子", ""))

        # 1. Reagent -> reaction type and family
        notes.append(
            AnkiNoteSpec(
                guid=stable_guid(card.slug, "reagent"),
                slug=card.slug,
                card_type="reagent",
                front=f"<code>{reagent_str}</code> (Ch10 Organohalides) 是什麼反應？family 與 stereo？",
                back=f"{card.name} (<code>{card.slug}</code>) — Family: {card.family} | Stereo: {stereo_str}",
                why=f"Intermediate：{interm_str}",
                tags=["ch10", card.slug, "reagent"],
            )
        )

        # 2. Regio-only
        if regio_str.lower() != "n/a" and not regio_str.lower().startswith("n/a"):
            notes.append(
                AnkiNoteSpec(
                    guid=stable_guid(card.slug, "regio"),
                    slug=card.slug,
                    card_type="regio",
                    front=f"<code>{reagent_str}</code> ({card.name}) 的 regio / 選擇性？",
                    back=regio_str,
                    why=f"{card.name} — Intermediate: {interm_str} ({card.family})",
                    tags=["ch10", card.slug, "regio"],
                )
            )

        # 3. Stereo-only
        if card.slug in STEREO_SLUGS and stereo_str.lower() != "n/a":
            notes.append(
                AnkiNoteSpec(
                    guid=stable_guid(card.slug, "stereo"),
                    slug=card.slug,
                    card_type="stereo",
                    front=f"<code>{reagent_str}</code> ({card.name}) 的立體化學 (stereo)？",
                    back=stereo_str,
                    why=f"Family: {card.family}；Intermediate: {interm_str}",
                    tags=["ch10", card.slug, "stereo"],
                )
            )

        # 4. Rearrangement
        if card.slug in REARRANGEMENT_SLUGS:
            notes.append(
                AnkiNoteSpec(
                    guid=stable_guid(card.slug, "rearrangement"),
                    slug=card.slug,
                    card_type="rearrangement",
                    front=f"<code>{reagent_str}</code> ({card.name}) 是否會發生 Rearrangement（重排／雙鍵移位）？",
                    back=rearr_str,
                    why=f"Intermediate: {interm_str}",
                    tags=["ch10", card.slug, "rearrangement"],
                )
            )

        # 5. Contrast cards
        if card.slug in CONTRAST_PROMPTS and contrast_str.lower() != "n/a":
            notes.append(
                AnkiNoteSpec(
                    guid=stable_guid(card.slug, "contrast"),
                    slug=card.slug,
                    card_type="contrast",
                    front=CONTRAST_PROMPTS[card.slug],
                    back=contrast_str,
                    why=f"{card.name}: intermediate = {interm_str}, regio = {regio_str}, stereo = {stereo_str}",
                    tags=["ch10", card.slug, "contrast"],
                )
            )

        # 6. Prediction cards from vetted examples
        if examples_raw and examples_raw.upper() != "TODO":
            for line in examples_raw.splitlines():
                line = line.strip()
                if line.startswith("- "):
                    line = line[2:].strip()
                if not line or "→" not in line or line in seen_examples:
                    continue
                seen_examples.add(line)
                lhs, rhs = [part.strip() for part in line.split("→", 1)]
                reason, smiles = PREDICTION_META.get(
                    (card.slug, line),
                    (f"{card.name}: regio={regio_str}, stereo={stereo_str}", ""),
                )
                why_html = reason
                if smiles:
                    why_html += f"<details><summary>SMILES</summary><code>{smiles}</code></details>"
                notes.append(
                    AnkiNoteSpec(
                        guid=stable_guid(card.slug, "prediction", lhs),
                        slug=card.slug,
                        card_type="prediction",
                        front=f"預測產物：<code>{lhs}</code> → ?",
                        back=rhs,
                        why=why_html,
                        tags=["ch10", card.slug, "prediction"],
                    )
                )

        # 7. Pitfall cards (only if user filled in ## 易錯)
        if pitfall_raw and pitfall_raw.upper() != "TODO":
            pitfall_clean = clean_bullet(pitfall_raw)
            notes.append(
                AnkiNoteSpec(
                    guid=stable_guid(card.slug, "pitfall"),
                    slug=card.slug,
                    card_type="pitfall",
                    front=f"{card.name} (<code>{reagent_str}</code>) 的常見易錯點為何？",
                    back=pitfall_clean,
                    why=f"Regio: {regio_str} | Stereo: {stereo_str} | Rearrangement: {rearr_str}",
                    tags=["ch10", card.slug, "pitfall"],
                )
            )

    return notes


def export_deck_and_csv(notes: list[AnkiNoteSpec]) -> None:
    deck = genanki.Deck(DECK_ID, DECK_NAME)
    for spec in notes:
        tags_str = " ".join(spec.tags)
        anki_note = genanki.Note(
            model=ANKI_MODEL,
            fields=[spec.front, spec.back, spec.why, tags_str],
            tags=spec.tags,
            guid=spec.guid,
        )
        deck.add_note(anki_note)

    genanki.Package(deck).write_to_file(str(APKG_PATH))

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["GUID", "Front", "Back", "Why", "Tags"])
        for spec in notes:
            writer.writerow([spec.guid, spec.front, spec.back, spec.why, " ".join(spec.tags)])


def main() -> None:
    card_files = sorted(CARDS_DIR.glob("*.md"))
    cards = [parse_card(p) for p in card_files]
    notes = generate_notes(cards)
    export_deck_and_csv(notes)
    print(f"Built {APKG_PATH.name} and {CSV_PATH.name} with {len(notes)} notes from {len(cards)} reaction cards.")


if __name__ == "__main__":
    main()
