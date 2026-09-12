import logging
import pyautogui
import time
from typing import Tuple

class ClickProcessor:
    def __init__(self, interval: float = 0.1):
        self.interval = max(0.01, min(interval, 60.0))
        self.logger = logging.getLogger(__name__)

    def execute_click(self, x: int, y: int) -> bool:
        try:
            screen_width, screen_height = pyautogui.size()
            if not (0 <= x < screen_width and 0 <= y < screen_height):
                raise ValueError(f"Coordinates ({x}, {y}) out of screen bounds")
            
            pyautogui.click(x, y)
            time.sleep(self.interval)
            return True
        except pyautogui.FailSafeException:
            self.logger.error("failsafe triggered by user")
            return False
        except Exception as e:
            self.logger.error(f"click execution failure: {e}")
            return False

    def batch_process(self, coordinates: list[Tuple[int, int]]) -> int:
        success_count = 0
        for x, y in coordinates:
            if self.execute_click(x, y):
                success_count += 1
        return success_count