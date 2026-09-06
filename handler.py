import time
import pyautogui
from threading import Thread, Event

class ClickHandler:
    def __init__(self, interval: float, button: str = 'left'):
        self.interval = interval
        self.button = button
        self._running = Event()
        self._thread = None

    def _run(self) -> None:
        while self._running.is_set():
            pyautogui.click(button=self.button)
            time.sleep(self.interval)

    def start(self) -> None:
        if not self._running.is_set():
            self._running.set()
            self._thread = Thread(target=self._run, daemon=True)
            self._thread.start()

    def stop(self) -> None:
        self._running.clear()
        if self._thread:
            self._thread.join()

    def update_interval(self, interval: float) -> None:
        self.interval = max(0.01, interval)