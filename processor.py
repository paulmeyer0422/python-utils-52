import time
import threading
from typing import Callable

class ClickProcessor:
    def __init__(self, interval: float):
        self.interval = interval
        self._running = False
        self._thread = None

    def _execute(self, action: Callable[[], None]) -> None:
        last_time = time.perf_counter()
        while self._running:
            action()
            next_time = last_time + self.interval
            sleep_time = next_time - time.perf_counter()
            if sleep_time > 0:
                time.sleep(sleep_time)
            last_time = time.perf_counter()

    def start(self, action: Callable[[], None]) -> None:
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._execute, args=(action,), daemon=True)
            self._thread.start()

    def stop(self) -> None:
        self._running = False
        if self._thread:
            self._thread.join()

    def update_interval(self, new_interval: float) -> None:
        self.interval = max(0.001, new_interval)