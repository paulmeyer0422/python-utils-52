def validate_click_params(interval: float, count: int) -> bool:
    if not isinstance(interval, (int, float)) or interval < 0.01:
        return False
    if not isinstance(count, int) or count < 0:
        return False
    return True

def validate_coordinates(x: int, y: int) -> bool:
    if not isinstance(x, int) or not isinstance(y, int):
        return False
    return x >= 0 and y >= 0

def sanitize_input(data: dict) -> dict:
    try:
        interval = float(data.get('interval', 0.1))
        count = int(data.get('count', 1))
        x = int(data.get('x', 0))
        y = int(data.get('y', 0))

        if validate_click_params(interval, count) and validate_coordinates(x, y):
            return {'interval': interval, 'count': count, 'x': x, 'y': y}
    except (ValueError, TypeError):
        pass
    return {'interval': 0.1, 'count': 1, 'x': 0, 'y': 0}