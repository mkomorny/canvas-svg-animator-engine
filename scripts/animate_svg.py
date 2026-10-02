#!/usr/bin/env python3
"""
Canvas SVG Animator Engine
Converts static SVG vector files and path strings into animated widgets:
- Laser Stroke Drawing (oscilloscope line drawing)
- Neon Pulse / Breathing Glow
- Radar / Gyro Spin
- Audio-Reactive HTML5 Canvas Visualizer
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path

ANIMATION_TEMPLATES = {
    "laser-trace": {
        "description": "Lines draw themselves onto the screen sequentially like a laser plotter or oscilloscope",
        "css": """
@keyframes svgLaserDraw {
  0% { stroke-dashoffset: 2000; opacity: 0; }
  10% { opacity: 1; }
  80% { stroke-dashoffset: 0; opacity: 1; }
  95% { stroke-dashoffset: 0; opacity: 1; }
  100% { stroke-dashoffset: 2000; opacity: 0; }
}
.animated-svg path, .animated-svg line, .animated-svg circle, .animated-svg polyline, .animated-svg polygon {
  stroke-dasharray: 2000;
  stroke-dashoffset: 2000;
  animation: svgLaserDraw 4s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}
"""
    },
    "pulse-glow": {
        "description": "Rhythmic neon glow and breathing intensity",
        "css": """
@keyframes neonPulse {
  0%, 100% { filter: drop-shadow(0 0 2px var(--glow, #00ffcc)) drop-shadow(0 0 8px var(--glow, #00ffcc)); opacity: 0.85; }
  50% { filter: drop-shadow(0 0 6px var(--glow, #00ffcc)) drop-shadow(0 0 20px var(--glow, #00ffcc)); opacity: 1; }
}
.animated-svg {
  animation: neonPulse 2.5s ease-in-out infinite;
}
"""
    },
    "spin": {
        "description": "Continuous smooth mechanical or radar sweep rotation",
        "css": """
@keyframes continuousSpin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
.animated-svg {
  transform-origin: center center;
  animation: continuousSpin 8s linear infinite;
}
"""
    },
    "combo": {
        "description": "Combined laser trace drawing + ambient breathing glow",
        "css": """
@keyframes svgLaserDraw {
  0% { stroke-dashoffset: 1500; opacity: 0; }
  15% { opacity: 1; }
  85% { stroke-dashoffset: 0; opacity: 1; }
  100% { stroke-dashoffset: 0; opacity: 1; }
}
@keyframes neonPulse {
  0%, 100% { filter: drop-shadow(0 0 2px var(--glow, #00ffcc)); }
  50% { filter: drop-shadow(0 0 10px var(--glow, #00ffcc)) drop-shadow(0 0 22px var(--glow, #00ffcc)); }
}
.animated-svg path, .animated-svg line, .animated-svg circle, .animated-svg polyline, .animated-svg polygon {
  stroke-dasharray: 1500;
  stroke-dashoffset: 1500;
  animation: svgLaserDraw 3.5s ease-out forwards;
}
.animated-svg {
  animation: neonPulse 3s ease-in-out infinite;
}
"""
    }
}

def animate_svg(svg_path_or_str, animation_mode="combo", glow_color="#00ffcc", bg_color="#07090c", out_path=None):
    # Check if input is a file or raw SVG code
    if os.path.exists(svg_path_or_str):
        with open(svg_path_or_str, "r", encoding="utf-8") as f:
            svg_content = f.read()
    else:
        svg_content = svg_path_or_str
        
    anim_data = ANIMATION_TEMPLATES.get(animation_mode, ANIMATION_TEMPLATES["combo"])
    css_rules = anim_data["css"]
    
    # Inject class into <svg>
    if 'class="' in svg_content:
        svg_content = svg_content.replace('class="', 'class="animated-svg ')
    else:
        svg_content = svg_content.replace('<svg ', '<svg class="animated-svg" ')
        
    html_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Canvas & SVG Animation · {animation_mode}</title>
  <style>
    :root {{
      --glow: {glow_color};
      --bg: {bg_color};
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      font-family: monospace;
      color: #fff;
      overflow: hidden;
    }}
    .stage {{
      position: relative;
      padding: 3rem;
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      background: radial-gradient(circle at center, rgba(0,255,200,0.03) 0%, rgba(0,0,0,0.6) 100%);
      box-shadow: 0 0 40px rgba(0, 0, 0, 0.8);
      max-width: 90vw;
      max-height: 85vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .animated-svg {{
      max-width: 650px;
      max-height: 650px;
      width: 100%;
      height: 100%;
    }}
    {css_rules}
    .badge {{
      position: absolute;
      top: 1rem;
      left: 1rem;
      background: rgba(255,255,255,0.06);
      padding: 0.3rem 0.7rem;
      border-radius: 4px;
      font-size: 0.75rem;
      color: var(--glow);
      border: 1px solid var(--glow)33;
    }}
  </style>
</head>
<body>
  <div class="stage">
    <div class="badge">MODE: {animation_mode.upper()} // GLOW: {glow_color}</div>
    {svg_content}
  </div>
</body>
</html>"""

    if not out_path:
        out_file = Path("./animated_svg_preview.html")
    else:
        out_file = Path(out_path)
        
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_page)
        
    return str(out_file.resolve()), css_rules

def main():
    parser = argparse.ArgumentParser(description="Animate SVG vectors with laser traces, glows, and spins.")
    parser.add_argument("--svg", required=True, help="Path to SVG file or inline SVG code")
    parser.add_argument("--mode", choices=["laser-trace", "pulse-glow", "spin", "combo"], default="combo", help="Animation mode")
    parser.add_argument("--glow", default="#00ffcc", help="Neon glow color")
    parser.add_argument("--out", default="./animated_preview.html", help="Destination HTML preview path")
    args = parser.parse_args()
    
    html_path, css = animate_svg(args.svg, animation_mode=args.mode, glow_color=args.glow, out_path=args.out)
    result = {
        "status": "success",
        "preview_path": html_path,
        "preview_uri": f"file:///{html_path.replace(chr(92), '/')}",
        "mode": args.mode,
        "css_code": css
    }
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
