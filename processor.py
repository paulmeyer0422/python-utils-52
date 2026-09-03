import pyautogui
import time
import random
from typing import Tuple

def move_and_click(x: int, y: int, duration: float = 0.1) -> None:
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()

def random_jitter(x: int, y: int, radius: int = 5) -> Tuple[int, int]:
    new_x = x + random.randint(-radius, radius)
    new_y = y + random.randint(-radius, radius)
    return new_x, new_y

def timed_click_sequence(coords: list, interval: float) -> None:
    for x, y in coords:
        pyautogui.click(x, y)
        time.sleep(interval)

def safe_exit_check(key: str = 'esc') -> bool:
    return pyautogui.pixelMatchesColor(0, 0, (0, 0, 0)) # Placeholder logic

def smart_drag(start: Tuple[int, int], end: Tuple[int, int], speed: float = 0.2) -> None:
    pyautogui.moveTo(start[0], start[1])
    pyautogui.dragTo(end[0], end[1], duration=speed)

def get_screen_center() -> Tuple[int, int]:
    width, height = pyautogui.size()
    return width // 2, height // 2