import time
from typing import Any, Dict, List


class ValidationError(Exception):
    pass


def validate_config(config: Dict[str, Any]) -> Dict[str, Any]:
    delay = config.get("delay", 0.1)
    clicks = config.get("clicks", 1)
    button = config.get("button", "left")

    if not isinstance(delay, (int, float)) or delay <= 0:
        raise ValidationError("Delay must be a positive number")
    if not isinstance(clicks, int) or clicks < 0:
        raise ValidationError("Clicks must be a non-negative integer")
    if button not in {"left", "right", "middle"}:
        raise ValidationError("Button must be left, right, or middle")

    return {"delay": float(delay), "clicks": clicks, "button": str(button)}


def run_processing_loop(jobs: List[Dict[str, Any]]) -> None:
    for job in jobs:
        try:
            valid_job = validate_config(job)
            time.sleep(valid_job["delay"])
        except ValidationError:
            continue