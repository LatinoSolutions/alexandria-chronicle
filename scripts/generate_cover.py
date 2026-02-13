#!/usr/bin/env python3
"""
Generate Alexandria Chronicle cover SVG.
Premium editorial design: modern-minimal with Victorian accents.
Standard library only. Deterministic output.
"""

import os

OUTPUT_PATH = "assets/chronicle-cover.svg"
W = 1600
H = 2200
MARGIN = 56
SAFE = 90

# Palette (exact)
PAPER_BG = "#F3EBD7"
PAPER_ALT = "#EFE4CC"
INK_MAIN = "#2F241A"
INK_SOFT = "#5A4A39"
LINE_HAIR = "#8A7762"
ACCENT = "#B08A57"

# Gradient for background
GRAD_TOP = "#F6EFDD"
GRAD_BOT = "#EFE4CC"

FONT = "Georgia, 'Times New Roman', serif"

# Content bounds (inside frame, 90px from inner frame edge)
FRAME_INNER = MARGIN + 28  # hairline frame
LEFT = FRAME_INNER + SAFE
RIGHT = W - FRAME_INNER - SAFE
CX = W // 2
CARD_PAD = 40
CARD_R = 10
LINE_HEIGHT = 44
HEADER_SIZE = 48
BODY_SIZE = 34
META_SIZE = 28


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    output = os.path.join(repo_root, OUTPUT_PATH)

    os.makedirs(os.path.dirname(output), exist_ok=True)

    # Frame box (triple frame inside margin)
    f1_x, f1_y = MARGIN, MARGIN
    f1_w, f1_h = W - 2 * MARGIN, H - 2 * MARGIN
    f2_inset = 12
    f3_inset = 28

    # Corner ornament (small filigree - diamond-inspired)
    co = 56
    corn = f'''<path d="M {co} {co} L {co} {co+20} M {co+10} {co+10} L {co+20} {co} M {co} {co+12} L {co+12} {co}" stroke="{INK_SOFT}" stroke-width="1" fill="none"/>'''

    # Build dot pattern (deterministic grid, subtle)
    dots_svg = []
    step = 36
    for i in range(step, W, step):
        for j in range(step, H, step):
            if (i ^ j) % 3 == 0:  # Deterministic sparse pattern
                dots_svg.append(f'<circle cx="{i}" cy="{j}" r="0.5" fill="{INK_MAIN}" opacity="0.04"/>')
    dots_str = "\n  ".join(dots_svg[:500])

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="paper" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:{GRAD_TOP}"/>
      <stop offset="100%" style="stop-color:{GRAD_BOT}"/>
    </linearGradient>
  </defs>

  <!-- Background: gradient + subtle texture -->
  <rect width="100%" height="100%" fill="url(#paper)"/>
  <g>{dots_str}</g>

  <!-- Triple frame -->
  <rect x="{f1_x}" y="{f1_y}" width="{f1_w}" height="{f1_h}" fill="none" stroke="{INK_MAIN}" stroke-width="4"/>
  <rect x="{f1_x+f2_inset}" y="{f1_y+f2_inset}" width="{f1_w-2*f2_inset}" height="{f1_h-2*f2_inset}" fill="none" stroke="{INK_SOFT}" stroke-width="1"/>
  <rect x="{f1_x+f3_inset}" y="{f1_y+f3_inset}" width="{f1_w-2*f3_inset}" height="{f1_h-2*f3_inset}" fill="none" stroke="{LINE_HAIR}" stroke-width="1"/>

  <!-- Corner ornaments (filigree) -->
  <g stroke="{INK_SOFT}" stroke-width="1.2" fill="none">
    <path d="M {84} {84} L {84} {100} M {92} {92} L {108} {84} M {84} {94} L {94} {84}"/>
    <path d="M {W-84} {84} L {W-84} {100} M {W-92} {92} L {W-108} {84} M {W-84} {94} L {W-94} {84}"/>
    <path d="M {84} {H-84} L {84} {H-100} M {92} {H-92} L {108} {H-84} M {84} {H-94} L {94} {H-84}"/>
    <path d="M {W-84} {H-84} L {W-84} {H-100} M {W-92} {H-92} L {W-108} {H-84} M {W-84} {H-94} L {W-94} {H-84}"/>
  </g>

  <!-- Top ornaments (centered, symmetric) -->
  <g stroke="{INK_SOFT}" stroke-width="1.5" fill="none">
    <line x1="{CX-320}" y1="148" x2="{CX-80}" y2="148"/>
    <line x1="{CX+80}" y1="148" x2="{CX+320}" y2="148"/>
    <polygon points="{CX-8},{140} {CX},{128} {CX+8},{140} {CX},{152}" fill="none" stroke="{INK_SOFT}" stroke-width="1"/>
  </g>
  <line x1="{LEFT}" y1="168" x2="{RIGHT}" y2="168" stroke="{LINE_HAIR}" stroke-width="1"/>

  <!-- Masthead -->
  <text x="{CX}" y="260" text-anchor="middle" font-family="{FONT}" font-size="84" font-weight="bold" letter-spacing="2" fill="{INK_MAIN}">ALEXANDRIA TOOLS CHRONICLE</text>
  <text x="{CX}" y="320" text-anchor="middle" font-family="{FONT}" font-size="30" font-style="italic" fill="{INK_SOFT}">Public Process • Private Edge</text>
  <rect x="{CX-95}" y="350" width="190" height="48" rx="24" ry="24" fill="{ACCENT}" fill-opacity="0.15" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="{CX}" y="384" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="bold" letter-spacing="2" fill="{INK_MAIN}">Issue 01</text>

  <!-- Card 1: Chronicle Edition -->
  <rect x="{LEFT}" y="430" width="{RIGHT-LEFT}" height="130" rx="{CARD_R}" ry="{CARD_R}" fill="{PAPER_ALT}" fill-opacity="0.4" stroke="{INK_SOFT}" stroke-width="1"/>
  <text x="{LEFT+CARD_PAD}" y="488" font-family="{FONT}" font-size="{HEADER_SIZE}" font-weight="bold" fill="{INK_MAIN}">◆ Chronicle Edition</text>
  <line x1="{LEFT+CARD_PAD}" y1="510" x2="{LEFT+CARD_PAD+200}" y2="510" stroke="{LINE_HAIR}" stroke-width="1"/>
  <text x="{LEFT+CARD_PAD}" y="548" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_MAIN}">• Issue 01 — 2026-02-13</text>

  <!-- Card 2: You Are Here (2-col grid) -->
  <rect x="{LEFT}" y="590" width="{RIGHT-LEFT}" height="240" rx="{CARD_R}" ry="{CARD_R}" fill="{PAPER_ALT}" fill-opacity="0.4" stroke="{INK_SOFT}" stroke-width="1"/>
  <text x="{LEFT+CARD_PAD}" y="648" font-family="{FONT}" font-size="{HEADER_SIZE}" font-weight="bold" fill="{INK_MAIN}">◆ You Are Here</text>
  <line x1="{LEFT+CARD_PAD}" y1="670" x2="{LEFT+CARD_PAD+220}" y2="670" stroke="{LINE_HAIR}" stroke-width="1"/>
  <text x="{LEFT+CARD_PAD}" y="718" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_SOFT}">Current Phase</text>
  <text x="{LEFT+380}" y="718" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_MAIN}">Contract Review</text>
  <text x="{LEFT+CARD_PAD}" y="766" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_SOFT}">Progress</text>
  <text x="{LEFT+380}" y="766" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_MAIN}">35%</text>
  <text x="{LEFT+CARD_PAD}" y="814" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_SOFT}">Status</text>
  <text x="{LEFT+378}" y="814" font-family="{FONT}" font-size="{BODY_SIZE}"><tspan fill="{ACCENT}">●</tspan> In Progress</text>
  <text x="{LEFT+CARD_PAD}" y="860" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_SOFT}">Next Gate</text>
  <text x="{LEFT+380}" y="860" font-family="{FONT}" font-size="{META_SIZE}" fill="{INK_MAIN}">Contract Review signed-off →</text>
  <text x="{LEFT+380}" y="900" font-family="{FONT}" font-size="{META_SIZE}" fill="{INK_MAIN}">move to Contract Visualization</text>

  <!-- Card 3: Roadmap Snapshot (2 columns) -->
  <rect x="{LEFT}" y="860" width="{RIGHT-LEFT}" height="520" rx="{CARD_R}" ry="{CARD_R}" fill="{PAPER_ALT}" fill-opacity="0.4" stroke="{INK_SOFT}" stroke-width="1"/>
  <text x="{LEFT+CARD_PAD}" y="918" font-family="{FONT}" font-size="{HEADER_SIZE}" font-weight="bold" fill="{INK_MAIN}">◆ Roadmap Snapshot</text>
  <line x1="{LEFT+CARD_PAD}" y1="940" x2="{LEFT+CARD_PAD+280}" y2="940" stroke="{LINE_HAIR}" stroke-width="1"/>
  <!-- Left column -->
  <text x="{LEFT+CARD_PAD}" y="990" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_MAIN}">☑ Project setup (Chronicle mock)</text>
  <text x="{LEFT+CARD_PAD}" y="1036" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_MAIN}">☐ Contract Review</text>
  <text x="{LEFT+CARD_PAD}" y="1082" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_MAIN}">☐ Contract Visualization</text>
  <text x="{LEFT+CARD_PAD}" y="1128" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_MAIN}">☐ Contract Corrections</text>
  <text x="{LEFT+CARD_PAD}" y="1174" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_MAIN}">☐ Human vs Logic Validator</text>
  <!-- Right column -->
  <text x="{CX}" y="990" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_MAIN}">☐ MT5 Implementation</text>
  <text x="{CX}" y="1036" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_MAIN}">☐ Data Gathering</text>
  <text x="{CX}" y="1082" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_MAIN}">☐ Feedback Loop</text>
  <text x="{CX}" y="1128" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_MAIN}">☐ Go Live</text>
  <text x="{CX}" y="1174" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_MAIN}">☐ Post-Live Monitoring</text>

  <!-- Card 4: Public vs Private -->
  <rect x="{LEFT}" y="1410" width="{RIGHT-LEFT}" height="180" rx="{CARD_R}" ry="{CARD_R}" fill="{PAPER_ALT}" fill-opacity="0.4" stroke="{INK_SOFT}" stroke-width="1"/>
  <text x="{LEFT+CARD_PAD}" y="1468" font-family="{FONT}" font-size="{HEADER_SIZE}" font-weight="bold" fill="{INK_MAIN}">◆ Public vs Private</text>
  <line x1="{LEFT+CARD_PAD}" y1="1490" x2="{LEFT+CARD_PAD+250}" y2="1490" stroke="{LINE_HAIR}" stroke-width="1"/>
  <text x="{LEFT+CARD_PAD}" y="1536" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_MAIN}">Public: roadmap milestones, implementation progress, validation updates.</text>
  <text x="{LEFT+CARD_PAD}" y="1582" font-family="{FONT}" font-size="{BODY_SIZE}" fill="{INK_MAIN}">Private: core strategy logic, exact thresholds, proprietary execution details.</text>

  <!-- Footer -->
  <line x1="{LEFT}" y1="1625" x2="{RIGHT}" y2="1625" stroke="{LINE_HAIR}" stroke-width="1"/>
  <text x="{CX}" y="1668" text-anchor="middle" font-family="{FONT}" font-size="{META_SIZE}" font-variant="small-caps" fill="{INK_SOFT}">Alexandria Tools Chronicle</text>
</svg>
'''

    with open(output, "w") as f:
        f.write(svg)

    print(f"Generated {output}")


if __name__ == "__main__":
    main()
