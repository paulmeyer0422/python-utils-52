import re
from typing import Any, Optional

def validate_interval(value: float) -> bool:
    return isinstance(value, (int, float)) and value > 0

def validate_coordinates(x: int, y: int) -> bool:
    return all(isinstance(val, int) and val >= 0 for val in (x, y))

def validate_key_binding(key: str) -> bool:
    if not isinstance(key, str) or len(key) > 1:
        return False
    return bool(re.match(r'[a-zA-Z0-9]', key))

def validate_click_count(count: int) -> bool:
    return isinstance(count, int) and (count > 0 or count == -1)

def sanitize_input(value: Any) -> Optional[Any]:
    if value is None:
        return None
    return str(value).strip()

def is_valid_config(config: dict) -> bool:
    required_keys = {'interval', 'x', 'y', 'key'}
    if not all(k in config for k in required_keys):
        return False
    return (
        validate_interval(config['interval']) and
        validate_coordinates(config['x'], config['y']) and
        validate_key_binding(config['key'])
    )