import re

def validate_coordinates(x: int, y: int) -> bool:
    return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0

def validate_interval(interval: float) -> bool:
    return isinstance(interval, (int, float)) and interval >= 0.001

def validate_hotkey(key: str) -> bool:
    if not isinstance(key, str) or len(key) == 0:
        return False
    return bool(re.match(r'^[a-zA-Z0-9]+$', key))

def validate_click_count(count: int) -> bool:
    return isinstance(count, int) and (count > 0 or count == -1)

def sanitize_input(value: str) -> str:
    return str(value).strip().lower()