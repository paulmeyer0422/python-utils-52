[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# python-utils-52

`python-utils-52` is a lightweight, high-performance auto-clicker built in Python for precise cursor automation and repetitive task simulation. It leverages low-level system APIs to deliver sub-millisecond click intervals with minimal CPU overhead.

## Features

* **Ultra-Low Latency:** Supports click intervals down to 1 millisecond with high-precision system-level threading.
* **Global Hotkey Listeners:** Instantly trigger, pause, or terminate clicking sequences from any active window using configurable keyboard shortcuts.
* **Smart Targeting:** Toggle between dynamic tracking of the current mouse position or locking onto fixed X/Y screen coordinates.
* **Anti-Detection Mode:** Optional randomized micro-delays (humanization) to naturally simulate manual human clicks.

## Installation

Ensure you have Python 3.8 or higher installed on your system. 

Clone the repository and install the required system dependencies:

```bash
git clone https://github.com/Developer/python-utils-52.git
cd python-utils-52
pip install -r requirements.txt
```

*(Note: On Linux systems, you may need to install `scrot` and `python3-tk` for coordinate tracking to function correctly.)*

## Quick Start

You can run the clicker via the command line or import the module directly into your own scripts.

### Basic Scripting Example

```python
import time
from python_utils_52 import AutoClicker

# Initialize clicker: 10 clicks per second, left-click
clicker = AutoClicker(interval=0.1, button='left')

# Start listening for global hotkeys (Default: [F1] to Start, [F2] to Stop)
clicker.bind_hotkeys(start_key='F1', stop_key='F2')

print("Auto-clicker active. Press F1 to start, F2 to stop.")
clicker.listen()
```

### Command Line Interface

To launch the utility immediately with default settings:

```bash
python main.py --interval 0.05 --button left
```