import time
import threading

class AutoClicker:
    def __init__(self, interval=0.1):
        self.interval = interval
        self.running = False
        self._thread = None

    def start(self):
        if not self.running:
            self.running = True
            self._thread = threading.Thread(target=self._click)
            self._thread.daemon = True
            self._thread.start()

    def stop(self):
        self.running = False
        if self._thread:
            self._thread.join()

    def _click(self):
        while self.running:
            self.perform_click()
            time.sleep(self.interval)

    @staticmethod
    def perform_click():
        print("Click performed")  # Simulated click action

# Example usage
if __name__ == '__main__':
    clicker = AutoClicker(0.1)
    clicker.start()
    time.sleep(1)
    clicker.stop()