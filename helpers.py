import random
import re
from typing import Tuple, List


def parse_delay(delay_str: str) -> float:
    match = re.match(r"^([\d.]+)\s*(ms|s)?$", delay_str.strip().lower())
    if not match:
        raise ValueError(f"Invalid delay format: {delay_str}")
    value, unit = match.groups()
    val = float(value)
    if unit == "ms":
        return val / 1000.0
    return val


def get_jittered_delay(base_delay: float, jitter: float) -> float:
    if jitter <= 0:
        return max(0.0, base_delay)
    min_val = max(0.0, base_delay - jitter)
    max_val = base_delay + jitter
    return random.uniform(min_val, max_val)


def validate_bounds(x: int, y: int, screen_size: Tuple[int, int]) -> Tuple[int, int]:
    width, height = screen_size
    clipped_x = max(0, min(x, width - 1))
    clipped_y = max(0, min(y, height - 1))
    return clipped_x, clipped_y


def generate_curve_points(
    start: Tuple[int, int], end: Tuple[int, int], steps: int = 10
) -> List[Tuple[int, int]]:
    points = []
    x1, y1 = start
    x2, y2 = end
    for i in range(steps + 1):
        t = i / steps
        curr_x = int(x1 + (x2 - x1) * t)
        curr_y = int(y1 + (y2 - y1) * t)
        points.append((curr_x, curr_y))
    return points
