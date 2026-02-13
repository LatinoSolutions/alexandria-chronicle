#!/usr/bin/env python3
"""
Generate Alexandria Chronicle cover SVG.
Standard library only. Victorian-modern sepia style.
Full newspaper layout with all Chronicle sections.
"""

import os

OUTPUT_PATH = "assets/chronicle-cover.svg"
W = 1600
H = 2200

# Sepia color palette
BG = "#f4ecd8"           # Warm sepia paper
INK = "#2b2118"          # Near-black brown (primary)
LINE = "#4a3a2a"         # Dark sepia (secondary)

# Typography: serif stack
FONT = "Georgia, 'Times New Roman', serif"

# Content area (inside frame)
MARGIN = 80
LEFT = MARGIN
RIGHT = W - MARGIN
CX = W // 2


def hrule(y, color=LINE):
    """Horizontal separator line."""
    return f'  <line x1="{LEFT}" y1="{y}" x2="{RIGHT}" y2="{y}" stroke="{color}" stroke-width="1"/>'


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    output = os.path.join(repo_root, OUTPUT_PATH)

    os.makedirs(os.path.dirname(output), exist_ok=True)

    inner_top, inner_left = 44, 44
    inner_w, inner_h = W - 88, H - 88
    inner_right = W - 44
    inner_bottom = H - 44

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <!-- Warm sepia background -->
  <rect width="100%" height="100%" fill="{BG}"/>
  <!-- Outer frame (secondary line) -->
  <rect x="28" y="28" width="{W-56}" height="{H-56}" fill="none" stroke="{LINE}" stroke-width="3"/>
  <!-- Inner frame (primary ink) -->
  <rect x="{inner_left}" y="{inner_top}" width="{inner_w}" height="{inner_h}" fill="none" stroke="{INK}" stroke-width="1"/>

  <!-- Victorian corner ornaments -->
  <g stroke="{INK}" stroke-width="1.5" fill="none">
    <path d="M 68 68 L 68 56 Q 68 48 76 48 L 68 48 M 68 58 L 78 48"/>
    <path d="M {W-68} 68 L {W-68} 56 Q {W-68} 48 {W-76} 48 L {W-68} 48 M {W-68} 58 L {W-78} 48"/>
    <path d="M 68 {H-68} L 68 {H-56} Q 68 {H-48} 76 {H-48} L 68 {H-48} M 68 {H-58} L 78 {H-48}"/>
    <path d="M {W-68} {H-68} L {W-68} {H-56} Q {W-68} {H-48} {W-76} {H-48} L {W-68} {H-48} M {W-68} {H-58} L {W-78} {H-48}"/>
  </g>

  <!-- Top decorative ornaments -->
  <g stroke="{INK}" stroke-width="1.5" fill="none">
    <line x1="140" y1="110" x2="500" y2="110"/>
    <line x1="140" y1="110" x2="160" y2="92"/>
    <line x1="260" y1="110" x2="260" y2="130"/>
    <line x1="380" y1="110" x2="380" y2="130"/>
    <line x1="500" y1="110" x2="480" y2="92"/>
  </g>
  <g stroke="{INK}" stroke-width="1.5" fill="none">
    <line x1="{W-140}" y1="110" x2="{W-500}" y2="110"/>
    <line x1="{W-140}" y1="110" x2="{W-160}" y2="92"/>
    <line x1="{W-260}" y1="110" x2="{W-260}" y2="130"/>
    <line x1="{W-380}" y1="110" x2="{W-380}" y2="130"/>
    <line x1="{W-500}" y1="110" x2="{W-480}" y2="92"/>
  </g>
  <line x1="520" y1="130" x2="{W-520}" y2="130" stroke="{LINE}" stroke-width="1"/>

  <!-- Masthead: Title -->
  <text x="{CX}" y="220" text-anchor="middle" font-family="{FONT}" font-size="56" font-weight="bold" letter-spacing="4" fill="{INK}">ALEXANDRIA TOOLS CHRONICLE</text>
  <!-- Subtitle -->
  <text x="{CX}" y="275" text-anchor="middle" font-family="{FONT}" font-size="24" font-style="italic" fill="{INK}">Public Process • Private Edge</text>
  <!-- Issue badge -->
  <rect x="{CX-90}" y="300" width="180" height="40" fill="none" stroke="{INK}" stroke-width="2"/>
  <text x="{CX}" y="328" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="bold" letter-spacing="3" fill="{INK}">Issue 01</text>

  <!-- Section 1: Chronicle Edition -->
{hrule(390)}
  <text x="{LEFT}" y="430" font-family="{FONT}" font-size="22" font-weight="bold" fill="{INK}">Chronicle Edition</text>
  <text x="{LEFT+30}" y="465" font-family="{FONT}" font-size="18" fill="{INK}">• Issue 01 — 2026-02-13</text>

  <!-- Section 2: You Are Here -->
{hrule(510)}
  <text x="{LEFT}" y="555" font-family="{FONT}" font-size="22" font-weight="bold" fill="{INK}">You Are Here</text>
  <text x="{LEFT+30}" y="595" font-family="{FONT}" font-size="18" fill="{INK}">Current Phase: Contract Review</text>
  <text x="{LEFT+30}" y="625" font-family="{FONT}" font-size="18" fill="{INK}">Progress: 35%</text>
  <text x="{LEFT+30}" y="655" font-family="{FONT}" font-size="18" fill="{INK}">Status: ● In Progress</text>
  <text x="{LEFT+30}" y="685" font-family="{FONT}" font-size="18" fill="{INK}">Next Gate: Contract Review signed-off → move to Contract Visualization</text>

  <!-- Section 3: Roadmap Snapshot -->
{hrule(735)}
  <text x="{LEFT}" y="775" font-family="{FONT}" font-size="22" font-weight="bold" fill="{INK}">Roadmap Snapshot</text>
  <text x="{LEFT+30}" y="815" font-family="{FONT}" font-size="18" fill="{INK}">☑ Project setup (Chronicle mock)</text>
  <text x="{LEFT+30}" y="850" font-family="{FONT}" font-size="18" fill="{INK}">☐ Contract Review</text>
  <text x="{LEFT+30}" y="885" font-family="{FONT}" font-size="18" fill="{INK}">☐ Contract Visualization</text>
  <text x="{LEFT+30}" y="920" font-family="{FONT}" font-size="18" fill="{INK}">☐ Contract Corrections</text>
  <text x="{LEFT+30}" y="955" font-family="{FONT}" font-size="18" fill="{INK}">☐ Human vs Logic Validator</text>
  <text x="{LEFT+30}" y="990" font-family="{FONT}" font-size="18" fill="{INK}">☐ MT5 Implementation</text>
  <text x="{LEFT+30}" y="1025" font-family="{FONT}" font-size="18" fill="{INK}">☐ Data Gathering</text>
  <text x="{LEFT+30}" y="1060" font-family="{FONT}" font-size="18" fill="{INK}">☐ Feedback Loop</text>
  <text x="{LEFT+30}" y="1095" font-family="{FONT}" font-size="18" fill="{INK}">☐ Go Live</text>
  <text x="{LEFT+30}" y="1130" font-family="{FONT}" font-size="18" fill="{INK}">☐ Post-Live Monitoring</text>

  <!-- Section 4: Public vs Private -->
{hrule(1175)}
  <text x="{LEFT}" y="1215" font-family="{FONT}" font-size="22" font-weight="bold" fill="{INK}">Public vs Private</text>
  <text x="{LEFT+30}" y="1255" font-family="{FONT}" font-size="18" fill="{INK}">Public: roadmap milestones, implementation progress, validation updates.</text>
  <text x="{LEFT+30}" y="1290" font-family="{FONT}" font-size="18" fill="{INK}">Private: core strategy logic, exact thresholds, proprietary execution details.</text>

  <!-- Bottom footer -->
{hrule(1345)}
  <text x="{CX}" y="1395" text-anchor="middle" font-family="{FONT}" font-size="20" fill="{LINE}">Alexandria Tools Chronicle</text>
</svg>
'''

    with open(output, "w") as f:
        f.write(svg)

    print(f"Generated {output}")


if __name__ == "__main__":
    main()
