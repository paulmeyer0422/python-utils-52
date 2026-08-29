import random
DEFAULT_INTERVAL = 0.05
MAX_CLICKS = 10000
MIN_INTERVAL = 0.001
BUTTONS = {
    "left": "left",
    "right": "right",
    "middle": "middle"
}
KEYBOARD_KEYS = {
    "start": "f8",
    "pause": "f9",
    "stop": "f10"
}
DEFAULT_POSITION = (0, 0)
SCREEN_RESOLUTION = (1920, 1080)
DELAY_TYPES = ["random", "fixed", "increasing"]
RANDOM_DELAY_MIN = 0.01
RANDOM_DELAY_MAX = 0.2

def calculate_delay(base_delay, variation):
    return base_delay + random.uniform(-variation, variation)

def get_button_from_string(btn_str):
    btn_str = btn_str.lower()
    if btn_str == "left":
        return "left"
    if btn_str == "right":
        return "right"
    if btn_str == "middle":
        return "middle"
    return "left"

def validate_interval(interval):
    return max(MIN_INTERVAL, min(interval, 1.0))

def get_hotkey(action):
    return KEYBOARD_KEYS.get(action)

def get_random_position():
    return (random.randint(0, SCREEN_RESOLUTION[0]), random.randint(0, SCREEN_RESOLUTION[1]))

def apply_delay_type(delay, delay_type, click_count):
    if delay_type == "random":
        return calculate_delay(delay, 0.05)
    elif delay_type == "increasing":
        return delay + (click_count * 0.001)
    return delay