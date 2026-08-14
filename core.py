import time

class AutoClicker:
    def __init__(self, interval=1.0):
        self.interval = interval
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            self.click()
            time.sleep(self.interval)

    def stop(self):
        self.running = False

    def click(self):
        print('Click!')  # Placeholder for actual click action

if __name__ == '__main__':
    clicker = AutoClicker(0.5)
    try:
        clicker.start()
    except KeyboardInterrupt:
        clicker.stop()