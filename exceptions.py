import time

class AutoclickerValidationError(Exception):
    pass


class InvalidClickPositionError(AutoclickerValidationError):
    pass


class InvalidIntervalError(AutoclickerValidationError):
    pass


class InvalidClickCountError(AutoclickerValidationError):
    pass


class InvalidButtonTypeError(AutoclickerValidationError):
    pass


def validate_click_position(x, y):
    if not isinstance(x, (int, float)):
        raise InvalidClickPositionError("x must be number")
    if not isinstance(y, (int, float)):
        raise InvalidClickPositionError("y must be number")
    if x < 0 or y < 0:
        raise InvalidClickPositionError("negative coordinates")
    if x > 3840 or y > 2160:
        raise InvalidClickPositionError("out of bounds")
    return True


def validate_interval(interval):
    if not isinstance(interval, (int, float)):
        raise InvalidIntervalError("interval must be number")
    if interval <= 0:
        raise InvalidIntervalError("interval must be positive")
    if interval > 3600:
        raise InvalidIntervalError("interval too large")
    return True


def validate_click_count(count):
    if not isinstance(count, int):
        raise InvalidClickCountError("count must be integer")
    if count <= 0:
        raise InvalidClickCountError("count must be positive")
    if count > 10000:
        raise InvalidClickCountError("count too large")
    return True


def validate_button(button):
    if button not in ("left", "right", "middle"):
        raise InvalidButtonTypeError("invalid button")
    return True


def run_processing_loop(positions, interval, count, button):
    validate_click_count(count)
    validate_interval(interval)
    validate_button(button)
    for _ in range(count):
        for x, y in positions:
            validate_click_position(x, y)
            time.sleep(interval)
    return count


if __name__ == "__main__":
    positions = [(100, 200), (300, 400)]
    try:
        result = run_processing_loop(positions, 0.1, 3, "left")
        print(result)
    except AutoclickerValidationError as e:
        print(e)