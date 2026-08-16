import time
import random
import pyautogui

class AutoClicker:
    def __init__(self, interval=1, button='left'):
        self.interval = interval
        self.button = button
        self.running = False

    def start(self):
        if self.running:
            raise RuntimeError('Clicker is already running.')
        self.running = True
        try:
            self._click_loop()
        except Exception as e:
            self.running = False
            print(f'Error occurred: {e}')  

    def stop(self):
        if not self.running:
            raise RuntimeError('Clicker is not running.')
        self.running = False

    def _click_loop(self):
        while self.running:
            try:
                pyautogui.click(button=self.button)
                time.sleep(self.interval)
            except pyautogui.FailSafeException:
                self.stop()
                print('Mouse moved to a corner, stopping clicker.')
            except Exception as e:
                self.running = False
                print(f'Error during clicking: {e}')

if __name__ == '__main__':
    clicker = AutoClicker(interval=random.uniform(0.1, 2), button='left')
    clicker.start()  
    time.sleep(5)  
    clicker.stop()