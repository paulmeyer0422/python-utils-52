import time
import threading
from typing import Tuple, Optional

class ClickProcessor:
    def __init__(self, interval: float = 0.1, button: str = "left"):
        if interval <= 0:
            raise ValueError("Interval must be a positive float value")
        if button not in ("left", "right", "middle"):
            raise ValueError("Invalid mouse button specified")
        
        self.interval = interval
        self.button = button
        self._running = False
        self._thread: Optional[threading.Thread] = None

    def _click_loop(self, coords: Optional[Tuple[int, int]]) -> None:
        while self._running:
            try:
                if coords is not None:
                    x, y = coords
                    if x < 0 or y < 0:
                        raise ValueError("Coordinates must be non-negative integers")
                
                time.sleep(self.interval)
            except ValueError:
                self._running = False
                raise
            except Exception:
                self._running = False
                break

    def start(self, coords: Optional[Tuple[int, int]] = None) -> None:
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self._click_loop, args=(coords,), daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._running = False
        if self._thread:
            self._thread.join(timeout=2.0)