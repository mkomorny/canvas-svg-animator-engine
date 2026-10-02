# Canvas SVG Animator Engine

[![Automated Release](https://img.shields.io/badge/release-automated_batch_pipeline-blue.svg)](https://github.com/mkomorny)
[![Pipeline Execution](https://img.shields.io/badge/dispatched_by-background_script-informational.svg)](https://github.com/mkomorny)

> [!NOTE]
> **Automated Distribution**: This repository was automatically sanitized, packaged, and published via a scheduled background batch staging pipeline. All file bundling, licensing, and repository synchronization were dispatched automatically by an automated release runner.

A high-performance vector graphics animation generator that transforms static SVG vector files and path coordinates into glowing, hardware-accelerated HTML5 Canvas and CSS animations.

## Animation Primitives

- **Laser Trace**: Simulates electron-beam oscilloscope or laser-plotter progressive stroke drawing (`stroke-dashoffset` path interpolation).
- **Neon Pulse**: Ambient harmonic breathing glow with multi-stop box/drop-shadow diffusion.
- **Radar & Gyro Spin**: Continuous angular velocity sweeps with customizable trail decay.
- **Oscilloscope Wave**: Dynamic sinusoidal path displacement for telemetry and audio-reactive interfaces.

## Features

- **CLI Generation**: Point at any `.svg` file or pass path coordinates to compile interactive animated HTML widgets.
- **Pure Vector Output**: Generates lightweight HTML/CSS/Canvas standalone files with zero external dependencies.
- **Customizable Timing**: Full control over cycle duration, easing functions, line thickness, and glow radius.

## Dependencies

- **Python**: Version 3.8 or higher (Standard Library: `os`, `sys`, `re`, `json`, `argparse`, `pathlib`). No third-party packages required.

## Instructions

See [INSTRUCTIONS.md](./INSTRUCTIONS.md) for command-line syntax and web integration.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0) - see the [LICENSE](./LICENSE) file for details.
