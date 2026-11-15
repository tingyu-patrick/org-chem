#!/usr/bin/env python3
"""Convert ch08/cards/*.md into an Anki deck (ch08_alkenes.apkg) and CSV (ch08_alkenes.csv)."""

from __future__ import annotations

import csv
import hashlib
import random
import re
from dataclasses import dataclass
from pathlib import Path
import genanki
import yaml

BASE_DIR = Path(__file__).resolve().parent
CARDS_DIR = BASE_DIR / "cards"
APKG_PATH = BASE_DIR / "ch08_alkenes.apkg"
CSV_PATH = BASE_DIR / "ch08_alkenes.csv"

DECK_NAME = "OrgChem::Ch08 Alkenes"
DECK_ID = 1849208108
MODEL_ID = 1607392819

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
    "OrgChem Ch08 Reaction Model",
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
    key = f"{slug}::{card_type}" if not extra else f"{slug}::{card_type}::{extra}"
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


# Non-trivial stereo slugs (omitting redundant pairs already tested in Reagent & Contrast cards)
STEREO_SLUGS = {
    "hx-addition",
    "x2-addition",
    "oxymercuration",
    "hydroboration",
    "epoxidation",
    "epoxide-hydrolysis",
    "oso4-hydroxylation",
}

# Non-trivial rearrangement slugs: carbocation vs bridged mercurinium vs concerted hydration
REARRANGEMENT_SLUGS = {
    "hx-addition",
    "oxymercuration",
    "hydroboration",
}

# Deduplicated contrast pairs (slug -> question prompt) so A vs B isn't asked twice identically
CONTRAST_PROMPTS = {
    "hx-addition": "對比：`HX addition` vs `oxymercuration` 的異同？",
    "halohydrin": "對比：`halohydrin` (`X2, H2O`) vs `x2-addition` (`X2, CH2Cl2`) 的差異？",
    "hydroboration": "對比：`hydroboration` vs `oxymercuration` 的水合結果差異？",
    "oso4-hydroxylation": "對比：`OsO4 hydroxylation` vs `epoxide-hydrolysis` (`RCO3H` then `H3O⁺`) 的 diol 立體化學？",
    "simmons-smith": "對比：`simmons-smith` vs `carbene-dichloro` 的試劑、中間體與產物差異？",
    "kmno4-cleavage": "對比：`kmno4-cleavage` (`KMnO4, H3O⁺`) vs `ozonolysis` (`O3; Zn/H3O⁺`) 的氧化程度？",
}

# One-line reasons and optional verified SMILES for the vetted examples
PREDICTION_META = {
    ("hx-addition", "1-methylcyclohexene + HBr → 1-bromo-1-methylcyclohexane"): (
        "Markovnikov addition via tertiary carbocation intermediate",
        "CC1(Br)CCCCC1",
    ),
    ("hx-addition", "3,3-dimethyl-1-butene + HBr → 2-bromo-2,3-dimethylbutane (rearranged, methyl shift)"): (
        "Markovnikov protonation gives 2° carbocation → 1,2-methyl shift to 3° carbocation → Br⁻ attack",
        "CC(C)C(C)(C)Br",
    ),
    ("oxymercuration", "1-methylcyclohexene + Hg(OAc)2/H2O; NaBH4 → 1-methylcyclohexanol"): (
        "Markovnikov hydration via mercurinium ion; NO rearrangement",
        "CC1(O)CCCCC1",
    ),
    ("oxymercuration", "3,3-dimethyl-1-butene + Hg(OAc)2/H2O; NaBH4 → 3,3-dimethyl-2-butanol (no rearrangement)"): (
        "Markovnikov hydration via mercurinium ion prevents methyl shift (NO rearrangement)",
        "CC(O)C(C)(C)C",
    ),
    ("hydroboration", "1-methylcyclohexene + BH3; H2O2/OH⁻ → trans-2-methylcyclohexanol"): (
        "anti-Markovnikov (OH on less substituted C) + syn addition (H and OH cis, so OH and CH3 are trans)",
        "C[C@@H]1CCCC[C@H]1O",
    ),
    ("x2-addition", "1-methylcyclohexene + Br2 → trans-1,2-dibromo-1-methylcyclohexane"): (
        "anti addition via bromonium ion opened by back-side Br⁻ attack",
        "C[C@]1(Br)CCCC[C@@H]1Br",
    ),
    ("epoxidation", "1-methylcyclohexene + RCO3H → 1-methyl-1,2-epoxycyclohexane; then H3O⁺ → trans diol"): (
        "RCO3H gives concerted syn epoxide (product); H3O⁺ opens protonated epoxide from the back (anti → trans-1,2-diol)",
        "CC12CCCCC1O2",
    ),
    ("oso4-hydroxylation", "1-methylcyclohexene + OsO4 → cis diol"): (
        "Concerted syn hydroxylation via cyclic osmate ester gives cis-1,2-diol",
        "C[C@]1(O)CCCC[C@H]1O",
    ),
    ("ozonolysis", "1-methylcyclohexene + O3; Zn → 6-oxoheptanal"): (
        "Reductive ozonolysis cleaves C=C and stops at ketone + aldehyde (no overoxidation)",
        "CC(=O)CCCCC=O",
    ),
    ("kmno4-cleavage", "1-methylcyclohexene + KMnO4/H3O⁺ → 6-oxoheptanoic acid"): (
        "Oxidative cleavage overoxidizes vinylic C–H to COOH while trisubstituted C= becomes ketone",
        "CC(=O)CCCCC(=O)O",
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
        examples_raw = strip_comments(card.sections.get("例子", ""))

        # 1. Reagent -> reaction type and family
        notes.append(
            AnkiNoteSpec(
                guid=stable_guid(card.slug, "reagent"),
                slug=card.slug,
                card_type="reagent",
                front=f"<code>{reagent_str}</code> 是什麼反應？family 與 stereo？",
                back=f"{card.name} (<code>{card.slug}</code>) — Family: {card.family} | Stereo: {stereo_str}",
                why=f"Intermediate：{interm_str}",
                tags=["ch08", card.slug, "reagent"],
            )
        )

        # 2. Regio-only (skip trivial n/a)
        if regio_str.lower() != "n/a" and not regio_str.lower().startswith("n/a"):
            notes.append(
                AnkiNoteSpec(
                    guid=stable_guid(card.slug, "regio"),
                    slug=card.slug,
                    card_type="regio",
                    front=f"<code>{reagent_str}</code> 的 regio？",
                    back=regio_str,
                    why=f"{card.name} — Intermediate: {interm_str} ({card.family})",
                    tags=["ch08", card.slug, "regio"],
                )
            )

        # 3. Stereo-only (focused non-trivial stereochemical reactions)
        if card.slug in STEREO_SLUGS and stereo_str.lower() != "n/a":
            notes.append(
                AnkiNoteSpec(
                    guid=stable_guid(card.slug, "stereo"),
                    slug=card.slug,
                    card_type="stereo",
                    front=f"<code>{reagent_str}</code> ({card.name}) 的 stereo (syn / anti / cannot say)？",
                    back=stereo_str,
                    why=f"Family: {card.family}；Intermediate: {interm_str}",
                    tags=["ch08", card.slug, "stereo"],
                )
            )

        # 4. Rearrangement yes/no (focus on non-trivial addition pathways)
        if card.slug in REARRANGEMENT_SLUGS:
            notes.append(
                AnkiNoteSpec(
                    guid=stable_guid(card.slug, "rearrangement"),
                    slug=card.slug,
                    card_type="rearrangement",
                    front=f"<code>{reagent_str}</code> ({card.name}) 是否會發生 Rearrangement？",
                    back=rearr_str,
                    why=f"Intermediate 為 {interm_str}（只有經由自由 carbocation 才會發生 rearrangement）",
                    tags=["ch08", card.slug, "rearrangement"],
                )
            )

        # 5. Contrast cards (deduplicated pairs)
        if card.slug in CONTRAST_PROMPTS and contrast_str.lower() != "n/a":
            notes.append(
                AnkiNoteSpec(
                    guid=stable_guid(card.slug, "contrast"),
                    slug=card.slug,
                    card_type="contrast",
                    front=CONTRAST_PROMPTS[card.slug],
                    back=contrast_str,
                    why=f"{card.name}: intermediate = {interm_str}, regio = {regio_str}, stereo = {stereo_str}",
                    tags=["ch08", card.slug, "contrast"],
                )
            )

        # 6. Prediction cards from vetted examples only
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
                        tags=["ch08", card.slug, "prediction"],
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
