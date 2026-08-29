import json
from pathlib import Path
from typing import Any, Dict

DEFAULTS = {
    "interval": 0.05,
    "button": "left",
    "hotkey": "ctrl+alt+c",
    "max_clicks": 100,
    "randomize": False,
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    config = DEFAULTS.copy()
    path = Path(config_path)
    if path.is_file():
        with path.open() as f:
            user_config = json.load(f)
        for key, value in user_config.items():
            if key in config:
                config[key] = value
    return config

def save_config(config: Dict[str, Any], config_path: str = "config.json") -> None:
    path = Path(config_path)
    with path.open("w") as f:
        json.dump(config, f, indent=2)
