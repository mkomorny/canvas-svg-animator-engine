---
name: canvas-svg-animator
description: Transforms static SVG graphics and vector paths into high-performance, glowing animations (laser-trace drawing, neon breathing pulse, continuous radar spin, and ambient oscilloscope glow). Triggered in chat whenever the user asks to animate an SVG, add glow effects, make a vector draw itself, or create an interactive animated graphic.
---

# Canvas & SVG Animator

Brings static vectors to life by generating smooth CSS and Canvas animations:
* **Laser-Trace Draw:** The vector draws its own outline stroke sequentially on screen like a laser plotter or oscilloscope.
* **Pulse / Neon Glow:** Ambient breathing neon glow and shadow bloom.
* **Radar Spin:** Continuous mechanical, gyro, or radar sweep rotation.
* **Combo:** Sequential laser stroke trace followed by looping neon breathing glow.

---

## When to Activate

Trigger this skill whenever the user says things like:
* *"Make this SVG icon or HUD graphic draw itself onto the screen."*
* *"Add a glowing neon pulse animation to this vector."*
* *"Create an animated radar sweep in SVG."*
* *"How do I animate this vector for my web app or synth UI?"*

---

## How to Execute Under the Hood (Silent Agent Workflow)

You do **NOT** ask the user to run scripts in PowerShell. Run the animator invisibly using terminal/bash commands:

```bash
# Animate an existing SVG file:
python "<skill_dir>/scripts/animate_svg.py" --svg "./hud_radar.svg" --mode "combo" --glow "#00ffcc" --out "./animated_radar.html"

# Animate with pure laser-draw:
python "<skill_dir>/scripts/animate_svg.py" --svg "./icon.svg" --mode "laser-trace" --glow "#ff5500" --out "./animated_icon.html"
```

The script returns:
1. An interactive `.html` showcase file that runs the animation smoothly in the browser.
2. The exact CSS keyframe snippet ready to copy/paste into any web app, Electron project, or dashboard.

---

## Chat Presentation Guidelines

When presenting the animation in chat:
1. Provide the clickable preview link: `[animated_graphic.html](file:///...)`
2. Provide the lightweight copy-paste CSS block so the user can easily drop the animation into their existing app styling.
