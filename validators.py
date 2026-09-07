from typing import Any, Tuple, Optional

class InputValidationError(Exception):
    pass

def validate_click_params(interval: Any, duration: Any) -> Tuple[float, float]:
    try:
        f_interval = float(interval)
        f_duration = float(duration)
    except (ValueError, TypeError):
        raise InputValidationError("Parameters must be numeric")

    if f_interval < 0.01:
        raise InputValidationError("Interval too low, minimum 0.01")
    if f_duration < 0:
        raise InputValidationError("Duration cannot be negative")

    return f_interval, f_duration

def validate_coordinates(x: Any, y: Any) -> Tuple[int, int]:
    try:
        i_x = int(x)
        i_y = int(y)
    except (ValueError, TypeError):
        raise InputValidationError("Coordinates must be integers")

    if i_x < 0 or i_y < 0:
        raise InputValidationError("Coordinates must be non-negative")

    return i_x, i_y

def sanitize_input(value: Any, default: Any = None) -> Any:
    if value is None:
        return default
    try:
        return str(value).strip()
    except Exception:
        return default