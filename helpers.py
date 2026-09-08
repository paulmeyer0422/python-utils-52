import random
import time
from typing import Tuple, Optional


def cps_to_interval(cps: float) -> float:
    if cps <= 0:
        raise ValueError("CPS must be greater than zero.")
    return 1.0 / cps


def apply_jitter(interval: float, jitter_percentage: float) -> float:
    if not 0 <= jitter_percentage <= 100:
        raise ValueError("Jitter percentage must be between 0 and 100.")
    if jitter_percentage == 0:
        return interval
    deviation = interval * (jitter_percentage / 100.0)
    return max(0.001, interval + random.uniform(-deviation, deviation))


def parse_coordinates(coords: str) -> Optional[Tuple[int, int]]:
    try:
        parts = coords.split(",")
        if len(parts) != 2:
            return None
        return int(parts[0].strip()), int(parts[1].strip())
    except ValueError:
        return None


def precise_sleep(duration: float) -> None:
    target = time.perf_counter() + duration
    while time.perf_counter() < target:
        remaining = target - time.perf_counter()
        if remaining > 0.01:
            time.sleep(remaining - 0.005)
