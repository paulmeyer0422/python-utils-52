import time
import pyautogui
from typing import Tuple

def move_and_click(coords: Tuple[int, int], clicks: int = 1, interval: float = 0.1) -> None:
    pyautogui.click(x=coords[0], y=coords[1], clicks=clicks, interval=interval)

def safe_execute(action, *args, **kwargs):
    try:
        return action(*args, **kwargs)
    except pyautogui.FailSafeException:
        return None

def drag_to(start: Tuple[int, int], end: Tuple[int, int], duration: float = 0.5) -> None:
    pyautogui.moveTo(*start)
    pyautogui.dragTo(*end, duration=duration)

def get_screen_size() -> Tuple[int, int]:
    return pyautogui.size()

def delay(seconds: float) -> None:
    time.sleep(seconds)

def capture_mouse_position() -> Tuple[int, int]:
    return pyautogui.position()