from typing import Any, Union


class ValidationError(Exception):
    pass


def validate_interval(value: Any) -> float:
    if not isinstance(value, (int, float)):
        raise ValidationError(f"Interval must be a number, got {type(value).__name__}")
    if value <= 0:
        raise ValidationError("Interval must be a positive number")
    return float(value)


def validate_coordinates(x: Any, y: Any) -> tuple[int, int]:
    try:
        xi, yi = int(x), int(y)
    except (ValueError, TypeError):
        raise ValidationError("Coordinates must be integers")
    if xi < 0 or yi < 0:
        raise ValidationError("Coordinates cannot be negative")
    return xi, yi


def validate_clicks(count: Any) -> int:
    if not isinstance(count, int) or count < 0:
        raise ValidationError("Click count must be a non-negative integer")
    return count