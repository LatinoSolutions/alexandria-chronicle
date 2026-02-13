#!/usr/bin/env python3
"""
Generate Alexandria Chronicle cover SVG.
Standard library only. Black-and-white newspaper/Victorian style.
"""

import os

OUTPUT_PATH = "assets/chronicle-cover.svg"
W = 1600
H = 900

# Font stack: serif-like fallback
FONT_TITLE = "Georgia, 'Times New Roman', Times, serif"
FONT_SUBTITLE = "Georgia, 'Times New Roman', Times, serif"
FONT_RIBBON = "Georgia, 'Times New Roman', Times, serif"
FONT_FOOTER = "Georgia, 'Times New Roman', Times, serif"


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    output = os.path.join(repo_root, OUTPUT_PATH)

    os.makedirs(os.path.dirname(output), exist_ok=True)

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <!-- White background -->
  <rect width="100%" height="100%" fill="#ffffff"/>
  <!-- Outer black frame -->
  <rect x="24" y="24" width="{W-48}" height="{H-48}" fill="none" stroke="#000000" stroke-width="4"/>
  <!-- Thin inner border -->
  <rect x="36" y="36" width="{W-72}" height="{H-72}" fill="none" stroke="#000000" stroke-width="1"/>

  <!-- Top decorative ornaments (geometric flourishes) -->
  <g stroke="#000000" stroke-width="2" fill="none">
    <!-- Left rule with ticks -->
    <line x1="80" y1="90" x2="420" y2="90"/>
    <line x1="120" y1="70" x2="120" y2="110"/>
    <line x1="250" y1="70" x2="250" y2="110"/>
    <line x1="380" y1="70" x2="380" y2="110"/>
    <!-- Right rule (mirror) -->
    <line x1="{W-80}" y1="90" x2="{W-420}" y2="90"/>
    <line x1="{W-120}" y1="70" x2="{W-120}" y2="110"/>
    <line x1="{W-250}" y1="70" x2="{W-250}" y2="110"/>
    <line x1="{W-380}" y1="70" x2="{W-380}" y2="110"/>
    <!-- Center flourish -->
    <line x1="{W//2-80}" y1="90" x2="{W//2+80}" y2="90"/>
    <line x1="{W//2}" y1="65" x2="{W//2}" y2="115"/>
    <line x1="{W//2-25}" y1="90" x2="{W//2+25}" y2="90"/>
  </g>

  <!-- Title -->
  <text x="{W//2}" y="280" text-anchor="middle" font-family="{FONT_TITLE}" font-size="72" font-weight="bold" fill="#000000">ALEXANDRIA TOOLS CHRONICLE</text>

  <!-- Subtitle -->
  <text x="{W//2}" y="360" text-anchor="middle" font-family="{FONT_SUBTITLE}" font-size="32" font-style="italic" fill="#000000">Public Process • Private Edge</text>

  <!-- Section ribbon -->
  <rect x="{W//2-120}" y="420" width="240" height="48" fill="none" stroke="#000000" stroke-width="2"/>
  <text x="{W//2}" y="452" text-anchor="middle" font-family="{FONT_RIBBON}" font-size="24" font-weight="bold" fill="#000000">Issue 01</text>

  <!-- Bottom text -->
  <text x="{W//2}" y="{H-80}" text-anchor="middle" font-family="{FONT_FOOTER}" font-size="20" fill="#000000">Newspaper-style Build Log</text>
</svg>
'''

    with open(output, "w") as f:
        f.write(svg)

    print(f"Generated {output}")


if __name__ == "__main__":
    main()
