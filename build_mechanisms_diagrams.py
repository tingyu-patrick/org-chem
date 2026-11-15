#!/usr/bin/env python3
"""Generate publication-quality ChemDraw-style SVG mechanism diagrams for Organic Chemistry Ch08 & Ch10."""

from __future__ import annotations
import html
import math
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent / "assets" / "mechanisms"
OUT_DIR.mkdir(parents=True, exist_ok=True)


class ChemSVG:
    """Lightweight ChemDraw-style vector canvas for multi-step reaction mechanisms."""

    def __init__(self, width: int = 980, height: int = 340, title: str = "") -> None:
        self.width = width
        self.height = height
        self.elements: list[str] = []
        self._add_header(title)

    def _add_header(self, title: str) -> None:
        self.elements.append(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" '
            f'width="100%" height="auto" style="background:#ffffff; font-family:\'Segoe UI\',Arial,sans-serif;">'
        )
        self.elements.append("""
  <defs>
    <marker id="el-arrow" markerWidth="8" markerHeight="8" refX="6.2" refY="4" orient="auto" markerUnits="strokeWidth">
      <path d="M0,1 L7,4 L0,7 L1.8,4 Z" fill="#dc2626"/>
    </marker>
    <marker id="fishhook" markerWidth="9" markerHeight="9" refX="6.5" refY="4.5" orient="auto" markerUnits="strokeWidth">
      <path d="M0,4.5 L7,4.5 L1.5,1 Z" fill="#dc2626"/>
    </marker>
    <marker id="rxn-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto" markerUnits="strokeWidth">
      <path d="M0,1.2 L8,4.5 L0,7.8 L1.8,4.5 Z" fill="#1e293b"/>
    </marker>
  </defs>""")
        self.elements.append(
            f'  <rect x="2" y="2" width="{self.width - 4}" height="{self.height - 4}" rx="10" '
            f'fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>'
        )
        if title:
            esc_title = html.escape(title)
            self.elements.append(
                f'  <rect x="2" y="2" width="{self.width - 4}" height="34" rx="10" fill="#f8fafc"/>'
                f'  <line x1="2" y1="36" x2="{self.width - 2}" y2="36" stroke="#e2e8f0" stroke-width="1"/>'
                f'  <text x="18" y="24" font-size="14" font-weight="700" fill="#0f172a">{esc_title}</text>'
            )

    def panel(self, x: float, y: float, w: float, h: float, label: str = "", bg: str = "#f8fafc") -> None:
        self.elements.append(
            f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{bg}" stroke="#e2e8f0" stroke-width="1"/>'
        )
        if label:
            esc_label = html.escape(label)
            self.elements.append(
                f'  <text x="{x + 10}" y="{y + 18}" font-size="12" font-weight="700" fill="#334155">{esc_label}</text>'
            )

    def bond(self, x1: float, y1: float, x2: float, y2: float, kind: str = "single", color: str = "#0f172a") -> None:
        dx, dy = x2 - x1, y2 - y1
        length = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / length, dx / length
        if kind == "single":
            self.elements.append(
                f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                f'stroke="{color}" stroke-width="2.2" stroke-linecap="round"/>'
            )
        elif kind == "double":
            off = 3.2
            self.elements.append(
                f'  <line x1="{x1 + nx*off:.1f}" y1="{y1 + ny*off:.1f}" x2="{x2 + nx*off:.1f}" y2="{y2 + ny*off:.1f}" '
                f'stroke="{color}" stroke-width="2.1" stroke-linecap="round"/>'
            )
            self.elements.append(
                f'  <line x1="{x1 - nx*off:.1f}" y1="{y1 - ny*off:.1f}" x2="{x2 - nx*off:.1f}" y2="{y2 - ny*off:.1f}" '
                f'stroke="{color}" stroke-width="2.1" stroke-linecap="round"/>'
            )
        elif kind == "dashed":
            self.elements.append(
                f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                f'stroke="{color}" stroke-width="2.0" stroke-dasharray="4,3" stroke-linecap="round"/>'
            )
        elif kind == "wedge":
            w = 4.5
            pts = f"{x1:.1f},{y1:.1f} {x2 + nx*w:.1f},{y2 + ny*w:.1f} {x2 - nx*w:.1f},{y2 - ny*w:.1f}"
            self.elements.append(f'  <polygon points="{pts}" fill="{color}"/>')
        elif kind == "hash":
            steps = 6
            for i in range(1, steps + 1):
                t = i / steps
                px, py = x1 + dx * t, y1 + dy * t
                hw = 4.5 * t
                self.elements.append(
                    f'  <line x1="{px - nx*hw:.1f}" y1="{py - ny*hw:.1f}" '
                    f'x2="{px + nx*hw:.1f}" y2="{py + ny*hw:.1f}" stroke="{color}" stroke-width="1.6"/>'
                )

    def atom(
        self,
        x: float,
        y: float,
        label: str,
        color: str = "#0f172a",
        size: int = 15,
        weight: str = "700",
        bg: bool = True,
        anchor: str = "middle",
    ) -> None:
        if bg and label:
            w = max(len(label) * (size * 0.58), 16)
            bx = x - w / 2 if anchor == "middle" else (x if anchor == "start" else x - w)
            self.elements.append(
                f'  <rect x="{bx:.1f}" y="{y - size + 2:.1f}" width="{w:.1f}" height="{size + 4:.1f}" fill="#ffffff" rx="3"/>'
            )
        esc_label = html.escape(label)
        self.elements.append(
            f'  <text x="{x:.1f}" y="{y + 5:.1f}" font-size="{size}" font-weight="{weight}" '
            f'fill="{color}" text-anchor="{anchor}">{esc_label}</text>'
        )

    def note(self, x: float, y: float, text: str, color: str = "#475569", size: int = 12, weight: str = "600", anchor: str = "middle") -> None:
        esc_text = html.escape(text)
        self.elements.append(
            f'  <text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" '
            f'fill="{color}" text-anchor="{anchor}">{esc_text}</text>'
        )

    def charge(self, x: float, y: float, symbol: str = "+", color: str = "#dc2626") -> None:
        esc_sym = html.escape(symbol)
        self.elements.append(
            f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="7.5" fill="#fef2f2" stroke="{color}" stroke-width="1.3"/>'
            f'  <text x="{x:.1f}" y="{y + 3.8:.1f}" font-size="11" font-weight="800" fill="{color}" text-anchor="middle">{esc_sym}</text>'
        )

    def curved_arrow(
        self,
        x1: float,
        y1: float,
        cx: float,
        cy: float,
        x2: float,
        y2: float,
        fishhook: bool = False,
    ) -> None:
        marker = "fishhook" if fishhook else "el-arrow"
        self.elements.append(
            f'  <path d="M {x1:.1f},{y1:.1f} Q {cx:.1f},{cy:.1f} {x2:.1f},{y2:.1f}" '
            f'fill="none" stroke="#dc2626" stroke-width="1.9" marker-end="url(#{marker})"/>'
        )

    def rxn_arrow(self, x1: float, y1: float, x2: float, y2: float, top: str = "", bottom: str = "") -> None:
        self.elements.append(
            f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="#1e293b" stroke-width="2.0" marker-end="url(#rxn-arrow)"/>'
        )
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        if top:
            esc_top = html.escape(top)
            self.elements.append(
                f'  <text x="{mx:.1f}" y="{my - 8:.1f}" font-size="11.5" font-weight="700" fill="#1e293b" text-anchor="middle">{esc_top}</text>'
            )
        if bottom:
            esc_bottom = html.escape(bottom)
            self.elements.append(
                f'  <text x="{mx:.1f}" y="{my + 16:.1f}" font-size="11" fill="#475569" text-anchor="middle">{esc_bottom}</text>'
            )

    def save(self, filename: str) -> Path:
        out = OUT_DIR / filename
        content = "\n".join(self.elements) + "\n</svg>\n"
        out.write_text(content, encoding="utf-8")
        return out


def draw_01_hx_addition() -> None:
    svg = ChemSVG(980, 320, "1. Hydrohalogenation (HX Addition) & Carbocation Rearrangement")
    svg.panel(16, 48, 300, 254, "Step 1: Protonation of Alkene (RDS)")
    svg.panel(336, 48, 300, 254, "Step 1b: 1,2-Shift (if 2° → 3° possible)")
    svg.panel(656, 48, 308, 254, "Step 2: Halide Nucleophilic Attack")

    # Panel 1: Alkene + H-Br
    svg.bond(85, 165, 145, 165, "double")
    svg.bond(85, 165, 55, 130); svg.atom(45, 122, "R", bg=False)
    svg.bond(85, 165, 55, 200); svg.atom(45, 208, "R", bg=False)
    svg.bond(145, 165, 175, 130); svg.atom(184, 122, "H", bg=False)
    svg.bond(145, 165, 175, 200); svg.atom(184, 208, "H", bg=False)
    svg.atom(85, 165, "C"); svg.atom(145, 165, "C")

    svg.bond(225, 165, 275, 165, "single")
    svg.atom(218, 165, "H"); svg.atom(282, 165, "Br:")
    svg.curved_arrow(115, 155, 165, 110, 212, 152)
    svg.curved_arrow(250, 158, 268, 125, 282, 148)
    svg.note(165, 255, "π electrons attack H; H adds to less sub. C", "#b91c1c")
    svg.rxn_arrow(305, 165, 345, 165, "slow")

    # Panel 2: Planar 3° Carbocation / 1,2-Methyl Shift
    svg.bond(435, 165, 505, 165, "single")
    svg.bond(435, 165, 405, 125); svg.atom(395, 118, "Me", bg=False)
    svg.bond(435, 165, 405, 205); svg.atom(395, 212, "Me", bg=False)
    svg.bond(435, 165, 435, 112); svg.atom(435, 102, "Me")
    svg.atom(435, 165, "C"); svg.atom(505, 165, "CH")
    svg.bond(505, 165, 545, 200); svg.atom(558, 208, "Me", bg=False)
    svg.charge(518, 138, "+")
    svg.curved_arrow(438, 128, 472, 95, 498, 148)
    svg.note(485, 240, "Planar sp² Carbocation (empty p orbital)", "#1e293b")
    svg.note(485, 262, "1,2-Hydride / Methyl shift if 2° → 3°", "#b91c1c")
    svg.rxn_arrow(625, 165, 665, 165, "fast")

    # Panel 3: Top/Bottom Br- attack -> Racemic
    svg.bond(770, 175, 835, 175, "single")
    svg.bond(770, 175, 740, 140); svg.atom(730, 132, "R", bg=False)
    svg.bond(770, 175, 740, 210); svg.atom(730, 218, "R", bg=False)
    svg.atom(770, 175, "C"); svg.atom(845, 175, "CH3")
    svg.charge(785, 152, "+")

    svg.atom(770, 95, ":Br", "#0f172a"); svg.charge(795, 88, "-")
    svg.atom(770, 255, ":Br", "#0f172a"); svg.charge(795, 248, "-")
    svg.curved_arrow(770, 110, 752, 138, 764, 158)
    svg.curved_arrow(770, 240, 752, 212, 764, 192)
    svg.note(875, 130, "50% Top attack", "#475569")
    svg.note(875, 225, "50% Bottom attack", "#475569")
    svg.note(810, 285, "Markovnikov | Not stereospecific (Racemic)", "#0f172a")
    svg.save("01-hx-addition.svg")


def draw_02_x2_addition() -> None:
    svg = ChemSVG(980, 320, "2. Halogenation (X2 Addition): Bridged Halonium Ion & Anti Opening")
    svg.panel(16, 48, 305, 254, "Step 1: Concerted Bromonium Formation")
    svg.panel(340, 48, 300, 254, "Step 2: Back-Side Attack by Br⁻")
    svg.panel(658, 48, 306, 254, "Product: trans-1,2-Dibromide (Anti)")

    # Panel 1
    svg.bond(115, 210, 185, 210, "double")
    svg.bond(115, 210, 85, 240, "wedge"); svg.bond(115, 210, 85, 180, "hash")
    svg.bond(185, 210, 215, 240, "wedge"); svg.bond(185, 210, 215, 180, "hash")
    svg.atom(115, 210, "C"); svg.atom(185, 210, "C")
    svg.bond(150, 125, 150, 78, "single")
    svg.atom(150, 132, ":Br:"); svg.atom(150, 72, ":Br:")
    svg.curved_arrow(142, 198, 112, 165, 136, 142)
    svg.curved_arrow(165, 138, 192, 168, 178, 196)
    svg.curved_arrow(156, 102, 185, 92, 166, 74)
    svg.note(165, 275, "Br lone pair back-donates → 3-membered ring", "#b91c1c")
    svg.rxn_arrow(310, 175, 350, 175)

    # Panel 2: Bromonium + back-side Br-
    svg.bond(445, 185, 525, 185, "single")
    svg.bond(445, 185, 485, 115, "single")
    svg.bond(525, 185, 485, 115, "single")
    svg.atom(445, 185, "C"); svg.atom(525, 185, "C"); svg.atom(485, 112, "Br")
    svg.charge(506, 98, "+")
    svg.atom(555, 255, ":Br"); svg.charge(578, 248, "-")
    svg.curved_arrow(545, 242, 545, 212, 530, 198)
    svg.curved_arrow(508, 152, 525, 122, 498, 112)
    svg.note(490, 282, "Top face blocked; Br⁻ attacks 180° back-side", "#b91c1c")
    svg.rxn_arrow(630, 175, 670, 175, "anti")

    # Panel 3: trans-1,2-dibromide
    svg.bond(765, 175, 845, 175, "single")
    svg.bond(765, 175, 765, 110, "wedge"); svg.atom(765, 98, "Br")
    svg.bond(845, 175, 845, 240, "hash"); svg.atom(845, 255, "Br")
    svg.bond(765, 175, 725, 210); svg.bond(845, 175, 885, 140)
    svg.atom(765, 175, "C"); svg.atom(845, 175, "C")
    svg.note(810, 282, "Strict Anti Addition | No Rearrangement", "#0f172a")
    svg.save("02-x2-addition.svg")


def draw_03_halohydrin() -> None:
    svg = ChemSVG(980, 320, "3. Halohydrin Formation (X2, H2O): Regioselective Anti Ring Opening")
    svg.panel(16, 48, 305, 254, "Step 1: Unsymmetrical Halonium Ion")
    svg.panel(340, 48, 310, 254, "Step 2: H2O Attacks More Substituted C")
    svg.panel(668, 48, 296, 254, "Step 3: Deprotonation → Halohydrin")

    # Panel 1
    svg.bond(115, 195, 195, 195, "single")
    svg.bond(115, 195, 160, 115, "dashed")
    svg.bond(195, 195, 160, 115, "single")
    svg.bond(115, 195, 75, 165); svg.atom(65, 158, "R", bg=False)
    svg.bond(115, 195, 75, 225); svg.atom(65, 232, "R", bg=False)
    svg.bond(195, 195, 235, 195); svg.atom(248, 195, "H", bg=False)
    svg.atom(115, 195, "C"); svg.atom(195, 195, "CH2"); svg.atom(160, 110, "Br")
    svg.charge(182, 96, "+")
    svg.note(115, 222, "δ+ (large)", "#dc2626", 12, "800")
    svg.note(165, 275, "More substituted C bears larger δ+ charge", "#475569")
    svg.rxn_arrow(310, 175, 350, 175)

    # Panel 2
    svg.bond(445, 175, 525, 175, "single")
    svg.bond(445, 175, 490, 105, "dashed")
    svg.bond(525, 175, 490, 105, "single")
    svg.atom(445, 175, "R2C"); svg.atom(525, 175, "CH2"); svg.atom(490, 102, "Br")
    svg.charge(510, 90, "+")
    svg.atom(425, 248, "H2O:", "#0284c7")
    svg.curved_arrow(435, 234, 422, 208, 438, 190)
    svg.curved_arrow(465, 142, 448, 112, 478, 104)
    svg.note(495, 278, "Solvent H2O outcompetes Br⁻ at more sub. C", "#b91c1c")
    svg.rxn_arrow(640, 175, 678, 175, "-H⁺")

    # Panel 3
    svg.bond(765, 175, 845, 175, "single")
    svg.bond(765, 175, 765, 240, "hash"); svg.atom(765, 255, "OH", "#0284c7")
    svg.bond(845, 175, 845, 110, "wedge"); svg.atom(845, 98, "Br")
    svg.atom(765, 175, "R2C"); svg.atom(845, 175, "CH2")
    svg.note(815, 282, "Markovnikov (OH on more sub. C) + Anti", "#0f172a")
    svg.save("03-halohydrin.svg")


def draw_04_oxymercuration() -> None:
    svg = ChemSVG(980, 320, "4. Oxymercuration–Demercuration: Mercurinium Ion & Radical NaBH4 Reduction")
    svg.panel(16, 48, 305, 254, "Step 1: Bridged Mercurinium Ion")
    svg.panel(340, 48, 310, 254, "Step 2: Back-Side H2O Attack at More Sub. C")
    svg.panel(668, 48, 296, 254, "Step 3: NaBH4 Scrambles Stereo (Radical)")

    # Panel 1
    svg.bond(110, 195, 195, 195, "single")
    svg.bond(110, 195, 155, 115, "dashed")
    svg.bond(195, 195, 155, 115, "single")
    svg.atom(110, 195, "R2C"); svg.atom(195, 195, "CH2")
    svg.atom(155, 110, "HgOAc"); svg.charge(192, 95, "+")
    svg.note(110, 222, "δ+ (large)", "#dc2626", 12, "800")
    svg.note(165, 275, "3-membered ring prevents carbocation shift", "#0f172a")
    svg.rxn_arrow(310, 175, 350, 175, "H2O")

    # Panel 2
    svg.bond(445, 175, 535, 175, "single")
    svg.bond(445, 175, 445, 240, "hash"); svg.atom(445, 255, "OH", "#0284c7")
    svg.bond(535, 175, 535, 110, "wedge"); svg.atom(535, 98, "HgOAc")
    svg.atom(445, 175, "R2C"); svg.atom(535, 175, "CHR'")
    svg.curved_arrow(535, 155, 565, 138, 545, 118, fishhook=True)
    svg.note(495, 278, "NaBH4 → R—Hg—H → homolysis to planar C•", "#b91c1c")
    svg.rxn_arrow(640, 175, 678, 175, "NaBH4")

    # Panel 3
    svg.bond(765, 175, 850, 175, "single")
    svg.bond(765, 175, 765, 240, "hash"); svg.atom(765, 255, "OH", "#0284c7")
    svg.bond(850, 175, 850, 112, "dashed"); svg.atom(850, 98, "H (wavy)")
    svg.atom(765, 175, "R2C"); svg.atom(850, 175, "CHR'")
    svg.note(815, 258, "+ Hg⁰↓ (scrambled syn/anti at C–H)", "#475569")
    svg.note(815, 282, "Markovnikov Alcohol | NO Rearrangement", "#0f172a")
    svg.save("04-oxymercuration.svg")


def draw_05_hydroboration() -> None:
    svg = ChemSVG(980, 340, "5. Hydroboration–Oxidation: 4-Center Syn TS & 1,2-Alkyl Shift with Retention")
    svg.panel(16, 48, 310, 274, "Part A: Concerted 4-Center Hydroboration")
    svg.panel(344, 48, 315, 274, "Part B1: HOO⁻ Attack & 1,2-Alkyl Shift")
    svg.panel(676, 48, 288, 274, "Part B2: Hydrolysis → Syn Alcohol")

    # Panel 1: 4-center TS
    svg.bond(110, 140, 210, 140, "double")
    svg.bond(110, 215, 210, 215, "single")
    svg.bond(110, 140, 110, 215, "dashed", "#64748b")
    svg.bond(210, 140, 210, 215, "dashed", "#64748b")
    svg.atom(110, 140, "R2C(δ+)"); svg.atom(210, 140, "CH2")
    svg.atom(110, 215, "H(δ-)"); svg.atom(210, 215, "BH2(δ-)", "#0284c7")
    svg.curved_arrow(160, 134, 195, 108, 210, 196)
    svg.curved_arrow(160, 215, 128, 195, 114, 156)
    svg.note(170, 265, "[4-Center Cyclic Transition State]‡", "#1e293b")
    svg.note(170, 288, "B attaches to less hindered C (same face as H)", "#b91c1c")
    svg.rxn_arrow(318, 180, 354, 180, "HOO⁻")

    # Panel 2: 1,2-alkyl shift on borate
    svg.bond(445, 180, 515, 180, "single")
    svg.bond(515, 180, 575, 180, "single")
    svg.bond(445, 180, 445, 115, "wedge")
    svg.atom(445, 102, "R* (chiral)")
    svg.atom(445, 180, "R2B"); svg.charge(422, 160, "-")
    svg.atom(515, 180, "O", "#0284c7"); svg.atom(580, 180, "OH")
    svg.curved_arrow(448, 145, 485, 130, 510, 166)
    svg.curved_arrow(545, 175, 562, 142, 578, 165)
    svg.note(500, 255, "1,2-Alkyl shift from B to O kicks out OH⁻", "#b91c1c")
    svg.note(500, 278, "100% Retention of configuration at migrating C!", "#0f172a")
    svg.rxn_arrow(650, 180, 686, 180, "H2O, OH⁻")

    # Panel 3: Final syn anti-Markovnikov alcohol
    svg.bond(770, 175, 855, 175, "single")
    svg.bond(770, 175, 770, 110, "wedge"); svg.atom(770, 98, "H")
    svg.bond(855, 175, 855, 110, "wedge"); svg.atom(855, 98, "OH", "#0284c7")
    svg.atom(770, 175, "R2C"); svg.atom(855, 175, "CH2")
    svg.note(818, 258, "H and OH on SAME face (Syn)", "#0284c7")
    svg.note(818, 282, "anti-Markovnikov | Syn | No Rearrangement", "#0f172a")
    svg.save("05-hydroboration.svg")


def draw_06_hydrogenation() -> None:
    svg = ChemSVG(980, 310, "6. Catalytic Hydrogenation (H2, Pd/C or PtO2): Syn Surface Transfer")
    svg.panel(16, 48, 305, 244, "Step 1: Surface Chemisorption of H2 & Alkene")
    svg.panel(340, 48, 305, 244, "Step 2: Sequential H Transfer (Same Face)")
    svg.panel(664, 48, 300, 244, "Step 3: Desorption of Syn Alkane")

    for px in (45, 370, 695):
        svg.bond(px, 235, px + 245, 235, "single", "#475569")
        svg.note(px + 122, 255, "Pd / Pt Metal Catalyst Surface", "#475569", 11)

    # Panel 1
    svg.bond(125, 145, 205, 145, "double")
    svg.atom(125, 145, "C"); svg.atom(205, 145, "C")
    svg.bond(95, 235, 95, 200, "single", "#0284c7"); svg.atom(95, 192, "H", "#0284c7")
    svg.bond(235, 235, 235, 200, "single", "#0284c7"); svg.atom(235, 192, "H", "#0284c7")
    svg.bond(165, 152, 165, 230, "dashed", "#64748b")
    svg.rxn_arrow(312, 165, 348, 165)

    # Panel 2
    svg.bond(450, 155, 530, 155, "single")
    svg.bond(450, 155, 450, 210, "wedge", "#0284c7"); svg.atom(450, 220, "H", "#0284c7")
    svg.bond(530, 155, 530, 235, "dashed", "#64748b")
    svg.bond(565, 235, 565, 200, "single", "#0284c7"); svg.atom(565, 192, "H", "#0284c7")
    svg.curved_arrow(560, 205, 548, 180, 535, 168)
    svg.atom(450, 155, "C"); svg.atom(530, 155, "C")
    svg.rxn_arrow(636, 165, 672, 165)

    # Panel 3
    svg.bond(770, 140, 855, 140, "single")
    svg.bond(770, 140, 770, 198, "wedge", "#0284c7"); svg.atom(770, 210, "H", "#0284c7")
    svg.bond(855, 140, 855, 198, "wedge", "#0284c7"); svg.atom(855, 210, "H", "#0284c7")
    svg.atom(770, 140, "C"); svg.atom(855, 140, "C")
    svg.note(815, 280, "Both H atoms delivered to same face (Syn)", "#0f172a")
    svg.save("06-hydrogenation.svg")


def draw_07_epoxidation() -> None:
    svg = ChemSVG(980, 330, "7. Epoxidation (RCO3H / mCPBA): Concerted Butterfly Transition State")
    svg.panel(16, 48, 520, 264, "Single Concerted Step: Butterfly Transition State (4 Curved Arrows)")
    svg.panel(560, 48, 404, 264, "Products: Stereospecific Syn Epoxide + RCO2H")

    # Left: Butterfly TS
    svg.bond(140, 240, 230, 240, "double")
    svg.atom(140, 240, "C"); svg.atom(230, 240, "C")
    svg.bond(140, 240, 100, 270, "wedge"); svg.bond(230, 240, 270, 270, "wedge")

    # Peroxyacid above alkene
    svg.atom(185, 165, "O", "#0284c7")
    svg.bond(185, 165, 255, 165, "single")
    svg.atom(255, 165, "O")
    svg.bond(255, 165, 290, 115, "single")
    svg.atom(290, 115, "C")
    svg.bond(290, 115, 350, 115, "single"); svg.atom(365, 115, "R'", bg=False)
    svg.bond(290, 115, 250, 75, "double"); svg.atom(242, 72, "O")
    svg.bond(185, 165, 165, 105, "single"); svg.atom(162, 95, "H")
    svg.bond(168, 92, 235, 74, "dashed", "#94a3b8")

    # 4 concerted arrows
    svg.curved_arrow(175, 232, 145, 198, 175, 175)
    svg.curved_arrow(176, 142, 212, 195, 224, 228)
    svg.curved_arrow(220, 165, 245, 132, 268, 135)
    svg.curved_arrow(265, 90, 215, 65, 174, 88)
    svg.note(275, 292, "① π→O  ② O–H→C  ③ O–O→C=O  ④ C=O→H", "#b91c1c")
    svg.rxn_arrow(525, 180, 570, 180, "concerted")

    # Right: Epoxide + RCO2H
    svg.bond(645, 210, 725, 210, "single")
    svg.bond(645, 210, 685, 140, "wedge", "#0284c7")
    svg.bond(725, 210, 685, 140, "wedge", "#0284c7")
    svg.atom(645, 210, "C"); svg.atom(725, 210, "C"); svg.atom(685, 132, "O", "#0284c7")
    svg.note(845, 180, "+  HO—C(=O)R'", "#334155", 14, "700")
    svg.note(760, 285, "Syn & Stereospecific (cis alkene → cis epoxide)", "#0f172a")
    svg.save("07-epoxidation.svg")


def draw_08_epoxide_hydrolysis() -> None:
    svg = ChemSVG(980, 320, "8. Acid-Catalyzed Epoxide Hydrolysis (H3O⁺): Anti Opening → trans-1,2-Diol")
    svg.panel(16, 48, 305, 254, "Step 1: Reversible Protonation of Epoxide")
    svg.panel(340, 48, 310, 254, "Step 2: Back-Side Attack by H2O")
    svg.panel(668, 48, 296, 254, "Step 3: Deprotonation → trans-1,2-Diol")

    # Panel 1
    svg.bond(110, 200, 190, 200, "single")
    svg.bond(110, 200, 150, 130, "single")
    svg.bond(190, 200, 150, 130, "single")
    svg.atom(110, 200, "C"); svg.atom(190, 200, "C"); svg.atom(150, 125, ":O:")
    svg.atom(245, 125, "H—OH2⁺", "#dc2626")
    svg.curved_arrow(165, 120, 195, 95, 218, 118)
    svg.note(165, 275, "Protonation converts O into good leaving group", "#475569")
    svg.rxn_arrow(310, 175, 350, 175)

    # Panel 2
    svg.bond(445, 180, 525, 180, "single")
    svg.bond(445, 180, 485, 110, "single")
    svg.bond(525, 180, 485, 110, "single")
    svg.atom(445, 180, "C"); svg.atom(525, 180, "C"); svg.atom(485, 105, "HO")
    svg.charge(508, 92, "+")
    svg.atom(430, 252, "H2O:", "#0284c7")
    svg.curved_arrow(438, 236, 425, 210, 440, 194)
    svg.curved_arrow(465, 145, 450, 118, 475, 108)
    svg.note(495, 278, "Water attacks from the back (inversion at C)", "#b91c1c")
    svg.rxn_arrow(640, 175, 678, 175, "-H⁺")

    # Panel 3
    svg.bond(765, 175, 845, 175, "single")
    svg.bond(765, 175, 765, 240, "hash"); svg.atom(765, 255, "OH", "#0284c7")
    svg.bond(845, 175, 845, 110, "wedge"); svg.atom(845, 98, "OH", "#dc2626")
    svg.atom(765, 175, "C"); svg.atom(845, 175, "C")
    svg.note(815, 282, "Anti Ring Opening → trans-1,2-diol", "#0f172a")
    svg.save("08-epoxide-hydrolysis.svg")


def draw_09_oso4_hydroxylation() -> None:
    svg = ChemSVG(980, 320, "9. Dihydroxylation (OsO4): Concerted [3+2] Cyclic Osmate Ester & Syn Cis-1,2-Diol")
    svg.panel(16, 48, 320, 254, "Step 1: Concerted [3+2] Cycloaddition")
    svg.panel(354, 48, 300, 254, "Intermediate: Cyclic Osmate(VI) Ester")
    svg.panel(672, 48, 292, 254, "Step 2: NaHSO3/H2O or NMO → cis-1,2-Diol")

    # Panel 1: Alkene + OsO4
    svg.bond(125, 220, 215, 220, "double")
    svg.atom(125, 220, "C"); svg.atom(215, 220, "C")
    svg.atom(170, 115, "Os(VIII)", "#0284c7")
    svg.bond(170, 115, 130, 165, "double"); svg.atom(125, 170, "O")
    svg.bond(170, 115, 210, 165, "double"); svg.atom(215, 170, "O")
    svg.bond(170, 115, 135, 75, "double"); svg.atom(128, 70, "O", bg=False)
    svg.bond(170, 115, 205, 75, "double"); svg.atom(212, 70, "O", bg=False)
    svg.curved_arrow(195, 212, 228, 195, 218, 178)
    svg.curved_arrow(195, 145, 195, 128, 182, 120)
    svg.curved_arrow(142, 152, 102, 185, 118, 210)
    svg.note(175, 278, "3 concerted arrows on same face of C=C", "#b91c1c")
    svg.rxn_arrow(328, 175, 362, 175)

    # Panel 2: Cyclic osmate ester
    svg.bond(455, 215, 545, 215, "single")
    svg.bond(455, 215, 455, 155, "wedge"); svg.atom(455, 148, "O")
    svg.bond(545, 215, 545, 155, "wedge"); svg.atom(545, 148, "O")
    svg.bond(455, 145, 500, 105, "single")
    svg.bond(545, 145, 500, 105, "single")
    svg.atom(500, 102, "OsO2", "#0284c7")
    svg.atom(455, 215, "C"); svg.atom(545, 215, "C")
    svg.note(502, 255, "5-Membered Cyclic Osmate(VI) Ester", "#1e293b")
    svg.note(502, 278, "Cleaves Os–O bonds (retains C–O stereo)", "#b91c1c")
    svg.rxn_arrow(644, 175, 680, 175, "NaHSO3 or NMO")

    # Panel 3: cis-1,2-diol
    svg.bond(770, 195, 855, 195, "single")
    svg.bond(770, 195, 770, 125, "wedge"); svg.atom(770, 112, "OH", "#0284c7")
    svg.bond(855, 195, 855, 125, "wedge"); svg.atom(855, 112, "OH", "#0284c7")
    svg.atom(770, 195, "C"); svg.atom(855, 195, "C")
    svg.note(815, 278, "Syn Hydroxylation → cis-1,2-diol", "#0f172a")
    svg.save("09-oso4-hydroxylation.svg")


def draw_10_carbene_dichloro() -> None:
    svg = ChemSVG(980, 320, "10. Dichlorocarbene Addition (CHCl3, KOH): α-Elimination & Syn Cyclopropanation")
    svg.panel(16, 48, 305, 254, "Step 1: Deprotonation of CHCl3")
    svg.panel(340, 48, 305, 254, "Step 2: α-Elimination → Singlet :CCl2")
    svg.panel(664, 48, 300, 254, "Step 3: Concerted Syn [2+1] Addition")

    # Panel 1
    svg.atom(75, 165, "HO:⁻", "#0284c7")
    svg.bond(145, 165, 195, 165, "single")
    svg.atom(138, 165, "H"); svg.atom(205, 165, "CCl3")
    svg.curved_arrow(95, 155, 115, 128, 132, 152)
    svg.curved_arrow(170, 158, 185, 128, 200, 152)
    svg.note(168, 265, "Forms trichloromethyl carbanion (⁻:CCl3)", "#475569")
    svg.rxn_arrow(312, 175, 348, 175, "-H2O")

    # Panel 2
    svg.bond(440, 165, 505, 165, "single")
    svg.atom(430, 165, "⁻:CCl2"); svg.atom(515, 165, "Cl:")
    svg.curved_arrow(475, 158, 492, 128, 510, 150)
    svg.note(490, 225, "→  :CCl2 (sp² lone pair + empty p orbital) + Cl⁻", "#0284c7")
    svg.note(490, 268, "α-Elimination (loss of H⁺ and Cl⁻ from same C)", "#b91c1c")
    svg.rxn_arrow(636, 175, 672, 175, "+ C=C")

    # Panel 3
    svg.bond(740, 215, 815, 215, "double")
    svg.atom(740, 215, "C"); svg.atom(815, 215, "C")
    svg.atom(778, 125, ":CCl2", "#0284c7")
    svg.curved_arrow(760, 206, 735, 165, 762, 135)
    svg.curved_arrow(795, 135, 822, 168, 808, 202)
    svg.note(895, 175, "→ 1,1-Cl2-cyclopropane", "#0f172a", 12, "700")
    svg.note(815, 278, "Concerted Syn & Stereospecific", "#0f172a")
    svg.save("10-carbene-dichloro.svg")


def draw_11_simmons_smith() -> None:
    svg = ChemSVG(980, 320, "11. Simmons–Smith Reaction (CH2I2, Zn(Cu)): Carbenoid Syn Cyclopropanation")
    svg.panel(16, 48, 305, 254, "Step 1: Carbenoid Generation")
    svg.panel(340, 48, 330, 254, "Step 2: 3-Center Concerted Transition State")
    svg.panel(688, 48, 276, 254, "Product: Stereospecific Cyclopropane")

    # Panel 1
    svg.note(168, 145, "I—CH2—I  +  Zn(Cu)", "#0f172a", 14, "700")
    svg.rxn_arrow(168, 165, 168, 205, "ether")
    svg.note(168, 232, "I—CH2—ZnI  (Carbenoid)", "#0284c7", 14, "700")
    svg.note(168, 275, "Electrophilic/nucleophilic CH2 transfer agent", "#475569")
    svg.rxn_arrow(312, 175, 348, 175)

    # Panel 2: 3-center TS
    svg.bond(445, 225, 535, 225, "double")
    svg.atom(445, 225, "C"); svg.atom(535, 225, "C")
    svg.atom(490, 145, "CH2", "#0284c7")
    svg.bond(490, 145, 450, 92, "single"); svg.atom(445, 85, "I")
    svg.bond(490, 145, 530, 92, "single"); svg.atom(538, 85, "ZnI")
    svg.bond(455, 85, 520, 85, "dashed", "#94a3b8")
    svg.curved_arrow(475, 216, 442, 180, 475, 155)
    svg.curved_arrow(512, 122, 545, 175, 530, 212)
    svg.curved_arrow(470, 118, 468, 92, 515, 88)
    svg.note(505, 278, "Concerted CH2 delivery + ZnI2 elimination", "#b91c1c")
    svg.rxn_arrow(660, 175, 696, 175)

    # Panel 3
    svg.bond(785, 215, 865, 215, "single")
    svg.bond(785, 215, 825, 140, "wedge", "#0284c7")
    svg.bond(865, 215, 825, 140, "wedge", "#0284c7")
    svg.atom(785, 215, "C"); svg.atom(865, 215, "C"); svg.atom(825, 132, "CH2", "#0284c7")
    svg.note(825, 252, "+  ZnI2", "#475569", 13, "700")
    svg.note(825, 280, "Syn & Stereospecific | No Rearrangement", "#0f172a")
    svg.save("11-simmons-smith.svg")


def draw_12_ozonolysis() -> None:
    svg = ChemSVG(980, 340, "12. Ozonolysis (1. O3; 2. Zn/H3O⁺): Molozonide → Criegee → Ozonide → Carbonyls")
    svg.panel(12, 48, 232, 274, "Step 1: [3+2] → Molozonide")
    svg.panel(256, 48, 236, 274, "Step 2: Cycloreversion")
    svg.panel(504, 48, 232, 274, "Step 3: [3+2] → Ozonide")
    svg.panel(748, 48, 220, 274, "Step 4: Reductive Workup")

    # Panel 1: O3 + C=C -> Molozonide
    svg.bond(85, 225, 165, 225, "double")
    svg.atom(85, 225, "C"); svg.atom(165, 225, "C")
    svg.atom(85, 145, "⁻O"); svg.atom(125, 115, "O⁺"); svg.atom(165, 145, "O")
    svg.bond(85, 145, 125, 115, "single"); svg.bond(125, 115, 165, 145, "double")
    svg.curved_arrow(145, 216, 178, 185, 165, 158)
    svg.curved_arrow(148, 128, 148, 102, 132, 108)
    svg.curved_arrow(85, 158, 68, 190, 82, 212)
    svg.note(128, 282, "Forms 1,2,3-trioxolane", "#475569")

    # Panel 2: Molozonide breaks C-C & O-O -> Carbonyl + Criegee
    svg.bond(330, 215, 415, 215, "single")
    svg.bond(330, 215, 330, 155, "single"); svg.atom(330, 148, "O")
    svg.bond(415, 215, 415, 155, "single"); svg.atom(415, 148, "O")
    svg.bond(330, 145, 372, 112, "single"); svg.bond(415, 145, 372, 112, "single")
    svg.atom(372, 108, "O"); svg.atom(330, 215, "C"); svg.atom(415, 215, "C")
    svg.curved_arrow(372, 215, 345, 192, 332, 178)
    svg.curved_arrow(352, 128, 355, 98, 372, 102)
    svg.curved_arrow(415, 162, 435, 185, 418, 202)
    svg.note(374, 265, "C–C & O–O cleave →", "#b91c1c")
    svg.note(374, 285, "R2C=O + R'2C=O⁺–O⁻ (Criegee)", "#0f172a")

    # Panel 3: Ozonide (1,2,4-trioxolane)
    svg.bond(575, 180, 620, 125, "single")
    svg.bond(665, 180, 620, 125, "single")
    svg.bond(575, 180, 592, 235, "single")
    svg.bond(665, 180, 648, 235, "single")
    svg.bond(592, 235, 648, 235, "single")
    svg.atom(620, 120, "O", "#0284c7")
    svg.atom(575, 180, "R2C"); svg.atom(665, 180, "CR'2")
    svg.atom(592, 235, "O", "#dc2626"); svg.atom(648, 235, "O", "#dc2626")
    svg.note(620, 275, "Ozonide (1,2,4-trioxolane)", "#1e293b")
    svg.note(620, 295, "Key textbook intermediate", "#0284c7")

    # Panel 4: Zn / H3O+ -> 2 Carbonyls
    svg.rxn_arrow(730, 180, 765, 180, "Zn/H3O⁺")
    svg.note(862, 155, "R2C = O", "#0f172a", 15, "700")
    svg.note(862, 185, "+", "#475569", 14, "700")
    svg.note(862, 215, "O = CR'2", "#0f172a", 15, "700")
    svg.note(858, 275, "Stops at Aldehyde / Ketone", "#0284c7")
    svg.note(858, 295, "(No overoxidation)", "#475569")
    svg.save("12-ozonolysis.svg")


def draw_13_kmno4_cleavage() -> None:
    svg = ChemSVG(980, 320, "13. KMnO4 Oxidative Cleavage (KMnO4, H3O⁺): Cyclic Manganate & Overoxidation")
    svg.panel(16, 48, 310, 254, "Step 1: [3+2] → Cyclic Manganate(V)")
    svg.panel(344, 48, 305, 254, "Step 2: C–C Oxidative Cleavage")
    svg.panel(668, 48, 296, 254, "Step 3: Overoxidation of C–H & =CH2")

    # Panel 1
    svg.bond(125, 215, 215, 215, "single")
    svg.bond(125, 215, 125, 155, "single"); svg.atom(125, 148, "O")
    svg.bond(215, 215, 215, 155, "single"); svg.atom(215, 148, "O")
    svg.bond(125, 145, 170, 105, "single"); svg.bond(215, 145, 170, 105, "single")
    svg.atom(170, 102, "MnO2⁻", "#7c3aed")
    svg.atom(125, 215, "R2C"); svg.atom(215, 215, "CHR'")
    svg.curved_arrow(170, 215, 142, 192, 128, 178)
    svg.curved_arrow(195, 128, 202, 105, 182, 102)
    svg.curved_arrow(215, 185, 232, 175, 218, 162)
    svg.note(170, 275, "5-Membered Cyclic Manganate Ester", "#475569")
    svg.rxn_arrow(318, 175, 354, 175, "H3O⁺")

    # Panel 2
    svg.note(495, 145, "R2C = O   (Ketone stays)", "#0f172a", 14, "700")
    svg.note(495, 180, "+", "#475569", 14, "700")
    svg.note(495, 215, "[ R'CH = O ]  (Aldehyde intermediate)", "#dc2626", 13, "700")
    svg.note(495, 275, "Aldehyde is immediately oxidized further!", "#b91c1c")
    svg.rxn_arrow(640, 175, 678, 175, "KMnO4/H3O⁺")

    # Panel 3
    svg.note(815, 135, "=CHR'  →  R'—COOH (Carboxylic acid)", "#b91c1c", 13, "700")
    svg.note(815, 185, "=CH2   →  [H2C=O] → CO2↑ + H2O", "#b91c1c", 13, "700")
    svg.note(815, 235, "=CR2   →  R2C=O (Ketone)", "#0f172a", 13, "700")
    svg.note(815, 280, "Overoxidizes vinylic C–H bonds", "#0f172a")
    svg.save("13-kmno4-cleavage.svg")


def draw_14_diol_cleavage() -> None:
    svg = ChemSVG(980, 320, "14. Periodate Cleavage of 1,2-Diols (HIO4, H2O): Cyclic Periodate Ester")
    svg.panel(16, 48, 315, 254, "Step 1: Condensation with HIO4")
    svg.panel(348, 48, 320, 254, "Step 2: Concerted 6-Electron Ring Cleavage")
    svg.panel(686, 48, 278, 254, "Products: 2 Carbonyls + HIO3")

    # Panel 1
    svg.bond(110, 145, 110, 215, "single")
    svg.bond(110, 145, 165, 145, "single"); svg.atom(175, 145, "OH", "#0284c7")
    svg.bond(110, 215, 165, 215, "single"); svg.atom(175, 215, "OH", "#0284c7")
    svg.atom(110, 145, "R2C"); svg.atom(110, 215, "R'2C")
    svg.note(255, 180, "+  HIO4", "#0f172a", 14, "700")
    svg.note(175, 275, "Diol OH groups attack I(VII) center (-H2O)", "#475569")
    svg.rxn_arrow(322, 175, 358, 175, "-H2O")

    # Panel 2: Cyclic periodate ester cleavage
    svg.bond(445, 140, 445, 220, "single")
    svg.bond(445, 140, 515, 140, "single"); svg.atom(515, 140, "O")
    svg.bond(445, 220, 515, 220, "single"); svg.atom(515, 220, "O")
    svg.bond(515, 140, 565, 180, "single")
    svg.bond(515, 220, 565, 180, "single")
    svg.atom(575, 180, "I(=O)2OH", "#0284c7")
    svg.atom(445, 140, "R2C"); svg.atom(445, 220, "R'2C")
    svg.curved_arrow(445, 180, 475, 205, 488, 216)
    svg.curved_arrow(538, 205, 562, 205, 562, 190)
    svg.curved_arrow(538, 155, 502, 122, 482, 136)
    svg.note(508, 275, "Cyclic Periodate Ester cleaves C–C bond", "#b91c1c")
    svg.rxn_arrow(658, 175, 694, 175)

    # Panel 3
    svg.note(825, 140, "R2C = O", "#0f172a", 15, "700")
    svg.note(825, 175, "+   R'2C = O", "#0f172a", 15, "700")
    svg.note(825, 215, "+   HIO3 [I(V)]", "#475569", 13, "700")
    svg.note(825, 278, "Converts 1,2-diol into 2 carbonyls", "#0f172a")
    svg.save("14-diol-cleavage.svg")


def draw_15_allylic_bromination() -> None:
    svg = ChemSVG(980, 340, "15. Allylic Bromination with NBS (Ch10): Radical Chain & Resonance Stabilization")
    svg.panel(12, 48, 235, 274, "1. Initiation & Allylic H Abstraction")
    svg.panel(258, 48, 255, 274, "2. Resonance-Stabilized Allylic Radical")
    svg.panel(524, 48, 215, 274, "3. NBS Role: Low [Br2] Supply")
    svg.panel(750, 48, 218, 274, "4. Propagation Step 2 → Product")

    # Panel 1: Fishhook abstraction of allylic H
    svg.bond(45, 175, 95, 175, "double")
    svg.bond(95, 175, 145, 175, "single")
    svg.bond(145, 175, 145, 115, "single")
    svg.atom(45, 175, "CH2"); svg.atom(95, 175, "CH"); svg.atom(145, 175, "CHR")
    svg.atom(145, 105, "H", "#0284c7")
    svg.atom(205, 105, "•Br:", "#dc2626")
    svg.curved_arrow(145, 145, 120, 152, 138, 165, fishhook=True)
    svg.curved_arrow(148, 132, 165, 92, 172, 102, fishhook=True)
    svg.curved_arrow(195, 102, 182, 92, 176, 102, fishhook=True)
    svg.note(128, 255, "Allylic C–H BDE is lowest", "#b91c1c")
    svg.note(128, 278, "(~364 kJ/mol vs 410 alkyl)", "#475569")

    # Panel 2: Resonance hybrid
    svg.note(385, 130, "CH2 = CH — C•H—R", "#0f172a", 13, "700")
    svg.note(385, 162, "⟷", "#0284c7", 18, "800")
    svg.note(385, 195, "•CH2 — CH = CH—R", "#0f172a", 13, "700")
    svg.note(385, 245, "Unpaired e⁻ delocalized over", "#0284c7")
    svg.note(385, 268, "allylic π system (never forms on", "#475569")
    svg.note(385, 288, "vinylic or unactivated alkyl C)", "#b91c1c")

    # Panel 3: NBS + HBr -> Br2
    svg.note(632, 135, "NBS  +  H—Br", "#0f172a", 13, "700")
    svg.rxn_arrow(632, 152, 632, 192, "ionic")
    svg.note(632, 215, "Succinimide + Br2 (trace)", "#0284c7", 12, "700")
    svg.note(632, 262, "Keeps [Br2] & [HBr] very low", "#b91c1c")
    svg.note(632, 284, "to prevent C=C ionic addition!", "#475569")

    # Panel 4: Allylic radical + Br2 -> Allylic bromide
    svg.note(858, 135, "Allylic•  +  Br—Br", "#0f172a", 13, "700")
    svg.rxn_arrow(858, 152, 858, 192, "fishhooks")
    svg.note(858, 215, "CH2=CH—CH(Br)R + •Br", "#0f172a", 12, "700")
    svg.note(858, 268, "Regenerates •Br chain carrier", "#0284c7")
    svg.save("15-allylic-bromination.svg")


def draw_16_alcohol_to_alkyl_halide() -> None:
    svg = ChemSVG(980, 360, "16. Alcohols → Alkyl Halides (Ch10): HX (SN1/SN2), SOCl2/py (SN2), PBr3 (SN2), DAST/HF")
    svg.panel(12, 48, 308, 294, "16A. 3° R–OH + HX (SN1 via Carbocation)")
    svg.panel(334, 48, 312, 294, "16B. 1°/2° R–OH + SOCl2 / Pyridine (SN2)")
    svg.panel(660, 48, 308, 294, "16C. 1°/2° R–OH + PBr3 (SN2) & 16D. R–F")

    # Panel 1: HX
    svg.note(165, 105, "R3C—OH  +  H—X  ⇌  R3C—OH2⁺ + X⁻", "#0f172a", 12, "700")
    svg.rxn_arrow(165, 120, 165, 160, "-H2O (RDS)")
    svg.note(165, 182, "R3C⁺ (3° Carbocation)  +  :X⁻", "#dc2626", 13, "700")
    svg.rxn_arrow(165, 196, 165, 236, "fast")
    svg.note(165, 258, "R3C—X  (SN1: fast for 3° alcohols)", "#0f172a", 13, "700")
    svg.note(165, 295, "*1° alcohols react with HBr via back-side SN2", "#475569", 11)
    svg.note(165, 315, "*2° alcohols + HX suffer rearrangement", "#b91c1c", 11)

    # Panel 2: SOCl2
    svg.note(490, 98, "R—OH + SOCl2 + py  →  R—O—S(=O)—Cl", "#0284c7", 12, "700")
    svg.note(490, 118, "(Alkyl chlorosulfite: good leaving group)", "#475569", 11)
    svg.bond(450, 195, 515, 195, "single")
    svg.bond(515, 195, 570, 195, "single")
    svg.atom(390, 195, ":Cl⁻", "#dc2626")
    svg.atom(450, 195, "C(R)"); svg.atom(515, 195, "O"); svg.atom(578, 195, "S(=O)Cl")
    svg.curved_arrow(408, 188, 425, 165, 442, 184)
    svg.curved_arrow(482, 190, 502, 162, 545, 182)
    svg.note(490, 255, "→  Cl—C(R) [100% Inversion] + SO2↑ + Cl⁻", "#0f172a", 12, "700")
    svg.note(490, 295, "SN2: No rearrangement! Ethers, carbonyls", "#0284c7", 11)
    svg.note(490, 315, "& aromatic rings don't interfere.", "#0284c7", 11)

    # Panel 3: PBr3 & DAST/HF
    svg.note(814, 98, "R—OH + PBr3  →  R—O⁺(H)—PBr2 + :Br⁻", "#0284c7", 12, "700")
    svg.bond(775, 175, 845, 175, "single")
    svg.atom(715, 175, ":Br⁻", "#dc2626")
    svg.atom(775, 175, "C(R)"); svg.atom(855, 175, "⁺O(H)PBr2")
    svg.curved_arrow(732, 168, 750, 145, 766, 164)
    svg.curved_arrow(805, 170, 825, 142, 842, 162)
    svg.note(814, 225, "→  Br—C(R) [SN2 Inversion] + HOPBr2", "#0f172a", 12, "700")
    svg.note(814, 275, "16D. Alkyl Fluorides (R–F):", "#b91c1c", 12, "700")
    svg.note(814, 298, "R–OH + [(CH3CH2)2NSF3] (DAST)", "#0f172a", 11, "700")
    svg.note(814, 318, "or HF / Pyridine  →  R–F ( up to 99% )", "#0f172a", 11, "700")
    svg.save("16-alcohol-to-alkyl-halide.svg")


def main() -> None:
    draw_01_hx_addition()
    draw_02_x2_addition()
    draw_03_halohydrin()
    draw_04_oxymercuration()
    draw_05_hydroboration()
    draw_06_hydrogenation()
    draw_07_epoxidation()
    draw_08_epoxide_hydrolysis()
    draw_09_oso4_hydroxylation()
    draw_10_carbene_dichloro()
    draw_11_simmons_smith()
    draw_12_ozonolysis()
    draw_13_kmno4_cleavage()
    draw_14_diol_cleavage()
    draw_15_allylic_bromination()
    draw_16_alcohol_to_alkyl_halide()
    print(f"Generated 16 SVG mechanism diagrams in {OUT_DIR}")


if __name__ == "__main__":
    main()
