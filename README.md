# Android Emulator Monitor + Optimizer

I built a tool that monitors and optimizes Android emulator performance using ADB and system-level metrics.

## Features

* Real-time emulator monitoring
* ADB-based metrics collection (CPU, Memory, FPS)
* Performance analysis + suggestions
* Host vs Emulator correlation
* Clean CLI output using `rich`

## Benchmarks

| Metric  | Emulator | Device |
| ------- | -------- | ------ |
| Startup | 1200ms   | 600ms  |

## Getting Started

1. Install requirements: `pip install -r requirements.txt`
2. Run monitor: `python main.py com.example.app`
