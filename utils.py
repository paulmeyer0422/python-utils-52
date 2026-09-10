import time
import pyautogui
from typing import Tuple, Optional

def perform_click(position: Tuple[int, int], interval: float = 0.1) -> None:
    """Execute mouse click at screen coordinates."""
    pyautogui.click(x=position[0], y=position[1])
    time.sleep(interval)

def get_mouse_position() -> Tuple[int, int]:
    """Retrieve current mouse cursor screen coordinates."""
    return pyautogui.position()

def safe_execute(action: callable, *args, **kwargs) -> Optional[any]:
    """Execute function with basic exception suppression."""
    try:
        return action(*args, **kwargs)
    except Exception:
        return None

class ClickerConfig:
    def __init__(self, delay: float, count: int) -> None:
        self.delay: float = delay
        self.count: int = count

def run_sequence(coords: Tuple[int, int], config: ClickerConfig) -> None:
    """Execute repeated clicks based on config."""
    for _ in range(config.count):
        perform_click(coords, config.delay)