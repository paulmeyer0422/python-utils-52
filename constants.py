import enum
from typing import Final

class ClickType(enum.Enum):
    LEFT = 'left'
    RIGHT = 'right'
    MIDDLE = 'middle'

class ActionState(enum.Enum):
    IDLE = 0
    RUNNING = 1
    PAUSED = 2

DEFAULT_INTERVAL: Final[float] = 0.1
MAX_CLICK_RATE: Final[float] = 1000.0
CONFIG_FILE: Final[str] = "config.json"

SETTINGS_SCHEMA: Final[dict] = {
    "interval": float,
    "button": str,
    "repeat": int,
    "hotkey": str
}

EXIT_KEYS: Final[list[str]] = ["esc", "f12"]

def get_default_config() -> dict:
    return {
        "interval": DEFAULT_INTERVAL,
        "button": ClickType.LEFT.value,
        "repeat": -1,
        "hotkey": "f9"
    }