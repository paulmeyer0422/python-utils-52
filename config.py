import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "hotkey": "f7",
    "click_type": "single",
    "hold_time": 0.0
}

class ConfigLoader:
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.config = self.load()

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.filepath):
            self.save(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                merged = DEFAULT_CONFIG.copy()
                merged.update({k: v for k, v in data.items() if k in DEFAULT_CONFIG})
                return merged
        except (json.JSONDecodeError, OSError):
            return DEFAULT_CONFIG.copy()

    def save(self, data: Dict[str, Any]) -> None:
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except OSError:
            pass

    def get(self, key: str) -> Any:
        return self.config.get(key, DEFAULT_CONFIG.get(key))
