#!/usr/bin/env python3
"""
Generate Alexandria Chronicle cover SVG.
Standard library only. Victorian-modern sepia style.
"""

import os

OUTPUT_PATH = "assets/chronicle-cover.svg"
W = 1600
H = 900

# Sepia color palette
BG = "#f4ecd8"           # Warm sepia paper
INK = "#2b2118"          # Near-black brown (primary)
LINE = "#4a3a2a"         # Dark sepia (secondary)

# Typography: serif stack
FONT = "Georgia, 'Times New Roman', serif"


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    output = os.path.join(repo_root, OUTPUT_PATH)
    cx = W // 2

    os.makedirs(os.path.dirname(output), exist_ok=True)

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <!-- Warm sepia background -->
  <rect width="100%" height="100%" fill="{BG}"/>
  <!-- Outer frame (secondary line) -->
  <rect x="28" y="28" width="{W-56}" height="{H-56}" fill="none" stroke="{LINE}" stroke-width="3"/>
  <!-- Inner frame (primary ink) -->
  <rect x="44" y="44" width="{W-88}" height="{H-88}" fill="none" stroke="{INK}" stroke-width="1"/>

  <!-- Victorian corner ornaments (symmetrical flourishes) -->
  <g stroke="{INK}" stroke-width="1.5" fill="none">
    <!-- Top-left -->
    <path d="M 68 68 L 68 56 Q 68 48 76 48 L 68 48 M 68 58 L 78 48"/>
    <!-- Top-right -->
    <path d="M {W-68} 68 L {W-68} 56 Q {W-68} 48 {W-76} 48 L {W-68} 48 M {W-68} 58 L {W-78} 48"/>
    <!-- Bottom-left -->
    <path d="M 68 {H-68} L 68 {H-56} Q 68 {H-48} 76 {H-48} L 68 {H-48} M 68 {H-58} L 78 {H-48}"/>
    <!-- Bottom-right -->
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
  <g stroke="{LINE}" stroke-width="1" fill="none">
    <line x1="520" y1="130" x2="{W-520}" y2="130"/>
  </g>

  <!-- Title -->
  <text x="{cx}" y="300" text-anchor="middle" font-family="{FONT}" font-size="68" font-weight="bold" letter-spacing="4" fill="{INK}">ALEXANDRIA TOOLS CHRONICLE</text>

  <!-- Subtitle -->
  <text x="{cx}" y="365" text-anchor="middle" font-family="{FONT}" font-size="28" font-style="italic" fill="{INK}">Public Process • Private Edge</text>

  <!-- Issue badge -->
  <rect x="{cx-100}" y="410" width="200" height="44" fill="none" stroke="{INK}" stroke-width="2"/>
  <text x="{cx}" y="440" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="bold" letter-spacing="3" fill="{INK}">Issue 01</text>

  <!-- Bottom caption (inside cover) -->
  <text x="{cx}" y="{H-70}" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{LINE}">Newspaper-style Build Log</text>
</svg>
'''

    with open(output, "w") as f:
        f.write(svg)

    print(f"Generated {output}")


if __name__ == "__main__":
    main()
