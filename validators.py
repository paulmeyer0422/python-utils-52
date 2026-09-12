from typing import Any, Tuple, Union


class ValidationError(ValueError):
    pass


def validate_interval(interval: Any) -> float:
    try:
        val = float(interval)
        if val <= 0:
            raise ValueError
        return val
    except (TypeError, ValueError):
        raise ValidationError(
            f"Interval must be a positive number, got {interval}"
        )


def validate_button(button: Any) -> str:
    allowed = {"left", "right", "middle"}
    if not isinstance(button, str) or button.lower() not in allowed:
        raise ValidationError(
            f"Button must be one of {allowed}, got {button}"
        )
    return button.lower()


def validate_click_count(count: Any) -> int:
    try:
        val = int(count)
        if val < 0:
            raise ValueError
        return val
    except (TypeError, ValueError):
        raise ValidationError(
            f"Click count must be a non-negative integer, got {count}"
        )


def validate_coordinates(coords: Any) -> Union[Tuple[int, int], None]:
    if coords is None:
        return None
    if (
        not isinstance(coords, (tuple, list))
        or len(coords) != 2
        or not all(isinstance(x, int) and x >= 0 for x in coords)
    ):
        raise ValidationError(
            f"Coordinates must be a tuple of two non-negative integers or None, got {coords}"
        )
    return (int(coords[0]), int(coords[1]))
