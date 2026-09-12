import time
import pyautogui
from typing import Tuple

def click_at(x: int, y: int, interval: float = 0.0) -> None:
    pyautogui.click(x, y)
    if interval > 0:
        time.sleep(interval)

def get_mouse_position() -> Tuple[int, int]:
    return pyautogui.position()

def safe_move(x: int, y: int, duration: float = 0.1) -> None:
    pyautogui.moveTo(x, y, duration=duration)

def perform_double_click(x: int, y: int) -> None:
    pyautogui.doubleClick(x, y)

def wait_for_seconds(seconds: float) -> None:
    time.sleep(seconds)

def is_pixel_color(x: int, y: int, rgb: Tuple[int, int, int], tolerance: int = 0) -> bool:
    pixel = pyautogui.pixel(x, y)
    if tolerance == 0:
        return pixel == rgb
    return all(abs(p - c) <= tolerance for p, c in zip(pixel, rgb))

def drag_mouse(x1: int, y1: int, x2: int, y2: int, duration: float = 0.5) -> None:
    pyautogui.moveTo(x1, y1)
    pyautogui.dragTo(x2, y2, duration=duration, button='left')