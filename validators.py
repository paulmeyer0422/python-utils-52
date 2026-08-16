from typing import Any, Dict, Optional


def validate_click_rate(click_rate: Optional[float]) -> float:
    """Validates the click rate.

    Args:
        click_rate (Optional[float]): The click rate to validate.

    Returns:
        float: A valid click rate. Raises ValueError if invalid.
    """
    if click_rate is None or click_rate <= 0:
        raise ValueError('Click rate must be a positive number.')
    return click_rate


def validate_duration(duration: Optional[int]) -> int:
    """Validates the duration.

    Args:
        duration (Optional[int]): The duration to validate.

    Returns:
        int: A valid duration. Raises ValueError if invalid.
    """
    if duration is None or duration <= 0:
        raise ValueError('Duration must be a positive integer.')
    return duration


def validate_position(position: Dict[str, Any]) -> Dict[str, int]:
    """Validates the position dictionary.

    Args:
        position (Dict[str, Any]): The position to validate.

    Returns:
        Dict[str, int]: A valid position dictionary. Raises KeyError if missing.
    """
    if 'x' not in position or 'y' not in position:
        raise KeyError('Position must include keys: x and y.')
    if not isinstance(position['x'], int) or not isinstance(position['y'], int):
        raise ValueError('Position coordinates must be integers.')
    return position
