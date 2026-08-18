import time
import threading

class AutoClicker:
    def __init__(self, interval: float = 0.1) -> None:
        """Initializes the AutoClicker with a specified interval.
        
        Args:
            interval (float): The time interval between clicks in seconds.
        """
        self.interval = interval
        self.running = False
        self.click_thread = threading.Thread(target=self._click)  

    def start(self) -> None:
        """Starts the auto clicker thread."""
        self.running = True
        self.click_thread.start()

    def stop(self) -> None:
        """Stops the auto clicker."""
        self.running = False
        self.click_thread.join()

    def _click(self) -> None:
        """Continuously performs clicks at the specified interval while running."""
        while self.running:
            self._perform_click()
            time.sleep(self.interval)

    def _perform_click(self) -> None:
        """Simulates a mouse click."""
        # This is a placeholder for actual click logic
        print("Click!")

if __name__ == '__main__':
    clicker = AutoClicker(0.5)
    clicker.start()
    time.sleep(2)
    clicker.stop()
