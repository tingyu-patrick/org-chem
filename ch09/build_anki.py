#!/usr/bin/env python3
"""Convert ch09/cards/*.md into an Anki deck (ch09_alkynes.apkg) and CSV (ch09_alkynes.csv)."""

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
APKG_PATH = BASE_DIR / "ch09_alkynes.apkg"
CSV_PATH = BASE_DIR / "ch09_alkynes.csv"

DECK_NAME = "OrgChem::Ch09 Alkynes"
DECK_ID = 1849208109
MODEL_ID = 1607392820

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
    "OrgChem Ch09 Reaction Model",
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
    key = f"ch09::{slug}::{card_type}" if not extra else f"ch09::{slug}::{card_type}::{extra}"
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
    "x2-addition-alkyne",
    "lindlar-reduction",
    "dissolving-metal-reduction",
    "acetylide-alkylation",
}

CONTRAST_PROMPTS = {
    "acetylide-deprotonation": "對比：為什麼去質子化末端炔要用 `NaNH2` 或 `BuLi`，而不能用 `KOH` / `NaOH`？",
    "acetylide-alkylation": "對比：`acetylide-alkylation` 對 `1° alkyl halide` vs `2°/3° alkyl halide` 的反應差異？",
    "hx-addition-alkyne": "對比：炔類加 `1 equiv HX` vs `2 equiv HX` 的產物差異與原因？",
    "hgso4-hydration": "對比：末端炔經 `H2SO4, H2O, HgSO4` vs `1. BH3; 2. H2O2, OH⁻` 的水合產物差異？",
    "lindlar-reduction": "對比：`H2, Lindlar catalyst` vs `Li, NH3(l)` 還原內部炔的立體化學差異？",
    "hydrogenation-complete": "對比：`2 H2, Pd/C` vs `H2, Lindlar catalyst` 對炔類的還原程度差異？",
    "alkyne-cleavage": "對比：炔類氧化斷裂 (`KMnO4` or `O3`) 與烯類臭氧化 (`O3; Zn`) 的產物差異？",
}

PREDICTION_META = {
    ("dehydrohalogenation", "1,2-dibromohexane + 2 NaNH2, NH3; then H3O⁺ → 1-hexyne"): (
        "Twofold E2 elimination of vicinal dibromide yields terminal alkyne after protonation",
        "CCCCC#C",
    ),
    ("acetylide-alkylation", "1-hexyne + 1. NaNH2, NH3; 2. CH3Br → 2-heptyne"): (
        "Deprotonation of terminal alkyne (pKa ~ 25) gives acetylide anion → SN2 on 1°/methyl halide",
        "CCCCC#CC",
    ),
    ("acetylide-alkylation", "propyne + 1. NaNH2, NH3; 2. 2-bromopropane → propene + propyne (E2 elimination, NOT alkylation!)"): (
        "2° and 3° alkyl halides undergo E2 elimination with strongly basic acetylide anions instead of SN2",
        "CC=C",
    ),
    ("hx-addition-alkyne", "1-hexyne + 1 equiv HBr → 2-bromo-1-hexene"): (
        "Markovnikov addition places Br on the more substituted internal sp carbon",
        "CCCCC(Br)=C",
    ),
    ("hx-addition-alkyne", "1-hexyne + 2 equiv HCl → 2,2-dichlorohexane (geminal dihalide)"): (
        "Second Markovnikov addition is directed to the same carbon by lone-pair resonance stabilization from the first Cl",
        "CCCCC(Cl)(Cl)C",
    ),
    ("x2-addition-alkyne", "1-hexyne + 1 equiv Cl2 → (E)-1,2-dichloro-1-hexene"): (
        "anti addition of Cl2 across triple bond gives trans-1,2-dichloroalkene",
        "CCCC/C(Cl)=C(\\H)Cl",
    ),
    ("x2-addition-alkyne", "2-butyne + 2 equiv Br2 → 2,2,3,3-tetrabromobutane"): (
        "Twofold halogen addition across triple bond yields tetrahalide",
        "CC(Br)(Br)C(C)(Br)Br",
    ),
    ("hgso4-hydration", "1-hexyne + H2O, H2SO4, HgSO4 → 2-hexanone (methyl ketone)"): (
        "Markovnikov hydration gives internal enol, which rapidly tautomerizes to methyl ketone",
        "CCCCC(=O)C",
    ),
    ("hydroboration-alkyne", "1-butyne + 1. BH3, THF; 2. H2O2, OH⁻ → butanal (CH3CH2CH2CHO)"): (
        "anti-Markovnikov hydration gives terminal enol, which tautomerizes to aldehyde",
        "CCCC=O",
    ),
    ("lindlar-reduction", "5-decyne + H2, Lindlar catalyst → cis-5-decene"): (
        "Concerted syn hydrogenation on poisoned Pd catalyst stops at cis-alkene",
        "CCCC/C=C\\CCCC",
    ),
    ("dissolving-metal-reduction", "5-decyne + Li, NH3 → trans-5-decene"): (
        "Dissolving metal reduction proceeds via trans-vinylic radical/anion to give trans-alkene",
        "CCCC/C=C/CCCC",
    ),
    ("alkyne-cleavage", "1-butyne + KMnO4, H3O⁺ (or O3; H2O) → propanoic acid (CH3CH2CO2H) + CO2"): (
        "Oxidative cleavage converts internal ≡C–R to RCO2H and terminal ≡CH to CO2",
        "CCC(=O)O",
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
                front=f"<code>{reagent_str}</code> (Ch09 Alkynes) 是什麼反應？family 與 stereo？",
                back=f"{card.name} (<code>{card.slug}</code>) — Family: {card.family} | Stereo: {stereo_str}",
                why=f"Intermediate：{interm_str}",
                tags=["ch09", card.slug, "reagent"],
            )
        )

        # 2. Regio-only (skip trivial n/a)
        if regio_str.lower() != "n/a" and not regio_str.lower().startswith("n/a"):
            notes.append(
                AnkiNoteSpec(
                    guid=stable_guid(card.slug, "regio"),
                    slug=card.slug,
                    card_type="regio",
                    front=f"<code>{reagent_str}</code> ({card.name}) 的 regio / 選擇性？",
                    back=regio_str,
                    why=f"{card.name} — Intermediate: {interm_str} ({card.family})",
                    tags=["ch09", card.slug, "regio"],
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
                    tags=["ch09", card.slug, "stereo"],
                )
            )

        # 4. Contrast cards
        if card.slug in CONTRAST_PROMPTS and contrast_str.lower() != "n/a":
            notes.append(
                AnkiNoteSpec(
                    guid=stable_guid(card.slug, "contrast"),
                    slug=card.slug,
                    card_type="contrast",
                    front=CONTRAST_PROMPTS[card.slug],
                    back=contrast_str,
                    why=f"{card.name}: intermediate = {interm_str}, regio = {regio_str}, stereo = {stereo_str}",
                    tags=["ch09", card.slug, "contrast"],
                )
            )

        # 5. Prediction cards from vetted examples
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
                        tags=["ch09", card.slug, "prediction"],
                    )
                )

        # 6. Pitfall cards (only if user filled in ## 易錯)
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
                    tags=["ch09", card.slug, "pitfall"],
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
