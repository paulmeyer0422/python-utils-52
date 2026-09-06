import re

def validate_coordinate(x: int, y: int) -> bool:
    return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0

def validate_interval(interval: float) -> bool:
    return isinstance(interval, (int, float)) and interval >= 0.001

def validate_button(button: str) -> bool:
    return button.lower() in ('left', 'right', 'middle')

def validate_hotkey(hotkey: str) -> bool:
    pattern = r'^[a-z0-9+]{1,20}$'
    return bool(re.match(pattern, hotkey.lower()))

def ensure_positive_integer(value: int) -> int:
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f'Expected positive integer, got {value}')
    return value

def sanitize_input_params(params: dict) -> dict:
    sanitized = {}
    for key, value in params.items():
        if value is not None:
            sanitized[key] = value
    return sanitized