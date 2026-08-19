import time
import threading

class AutoClicker:
    def __init__(self, interval=1):
        self.interval = interval
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._click_loop)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def _click_loop(self):
        while self.running:
            self._perform_click()
            time.sleep(self.interval)

    def _perform_click(self):
        print('Click!')  # Simulated click action

if __name__ == '__main__':
    autoclicker = AutoClicker(interval=0.5)
    autoclicker.start()
    time.sleep(5)
    autoclicker.stop()