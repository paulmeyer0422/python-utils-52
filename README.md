[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# python-utils-52

python-utils-52 is a lightweight Python autoclicker built for precise mouse automation. It handles repetitive clicking tasks with reliable timing and minimal system overhead.

## Features
- Configurable click intervals from 10ms to several seconds with optional randomization
- Support for left, right, and middle mouse buttons
- Global hotkey controls to start, stop, and adjust speed during operation
- Fixed-position clicking with optional human-like timing variance

## Installation

```bash
git clone https://github.com/Developer/python-utils-52.git
cd python-utils-52
pip install -r requirements.txt
```

## Basic Usage

```python
from python_utils_52 import AutoClicker

clicker = AutoClicker(interval=0.25, button="left")
clicker.start(duration=120)  # Run for 2 minutes
```

Use `clicker.stop()` or the configured hotkey to interrupt execution.