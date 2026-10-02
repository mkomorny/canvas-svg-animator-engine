# Canvas SVG Animator - Setup & Usage Guide

## Prerequisites
- **Python**: 3.8+

---

## 1. Quick Start

Generate an animated laser-trace widget from an SVG file:

```bash
python scripts/animate_svg.py --input logo.svg --effect laser-trace --output ./dist/animated_logo.html
```

---

## 2. Supported Effects

| Effect Flag | Description |
| :--- | :--- |
| `--effect laser-trace` | Progressive stroke drawing like an oscilloscope or laser plotter |
| `--effect neon-pulse` | Rhythmic breathing luminescence with multi-layer drop shadows |
| `--effect radar-spin` | Continuous rotating sweep reticle with phosphor decay |
| `--effect oscilloscope` | Dynamic wave oscillation |

---

## 3. Embedding in Web Projects

The generated HTML file contains inline CSS keyframes and SVG structures that can be pasted directly into React, Vue, or vanilla HTML components.
