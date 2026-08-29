import json
import os
from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional

@dataclass
class Config:
    click_interval: float = 0.05
    button: str = "left"
    start_key: str = "f8"
    stop_key: str = "esc"
    randomize: bool = False
    min_delay: float = 0.01
    max_delay: float = 0.1
    repeat_count: int = 0
    window_title: Optional[str] = None
    press_duration: float = 0.01
    post_click_delay: float = 0.0
    use_pynput: bool = True
    log_clicks: bool = False
    max_runtime: Optional[float] = None

def load_config(path: str = "config.json") -> Config:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            valid_keys = Config.__dataclass_fields__.keys()
            filtered_data = {k: v for k, v in data.items() if k in valid_keys}
            return Config(**filtered_data)
    return Config()

def save_config(config: Config, path: str = "config.json") -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(asdict(config), file, indent=2)

def validate(config: Config) -> bool:
    if config.click_interval <= 0:
        return False
    if config.button not in ["left", "right", "middle"]:
        return False
    if config.repeat_count < 0:
        return False
    if config.randomize and (config.min_delay < 0 or config.max_delay <= config.min_delay):
        return False
    return True

def merge(config: Config, updates: Dict[str, Any]) -> Config:
    for key, value in updates.items():
        if hasattr(config, key):
            setattr(config, key, value)
    return config

def reset() -> Config:
    return Config()

def get_default() -> Config:
    return Config()