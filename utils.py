import json
import os
from typing import Any, Dict


def load_config(filepath: str) -> Dict[str, Any]:
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def save_config(filepath: str, data: Dict[str, Any]) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def validate_cps(cps: float, min_cps: float = 0.1, max_cps: float = 100.0) -> float:
    return max(min_cps, min(cps, max_cps))


def calculate_delay(cps: float) -> float:
    validated = validate_cps(cps)
    return 1.0 / validated
