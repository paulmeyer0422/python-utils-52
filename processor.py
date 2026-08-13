from typing import Optional

class ClickProcessor:
    def __init__(self, click_interval: float) -> None:
        """Initialize the ClickProcessor with a click interval."""
        self.click_interval = click_interval

    def process_clicks(self, num_clicks: int, duration: Optional[float] = None) -> None:
        """Process the specified number of clicks, optionally timed by duration."""
        if duration is not None:
            self._process_with_duration(num_clicks, duration)
        else:
            self._process_without_duration(num_clicks)

    def _process_with_duration(self, num_clicks: int, duration: float) -> None:
        import time
        start_time = time.time()
        clicks_done = 0
        while time.time() - start_time < duration and clicks_done < num_clicks:
            self._click()
            clicks_done += 1
            time.sleep(self.click_interval)

    def _process_without_duration(self, num_clicks: int) -> None:
        for _ in range(num_clicks):
            self._click()
            time.sleep(self.click_interval)

    def _click(self) -> None:
        print('Click!') # Simulating a click action

