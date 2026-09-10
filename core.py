import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Any

@dataclass
class ClickProfile:
    interval: float
    button: str
    iterations: int

class ClickDataManager:
    def __init__(self, storage_path: str = "config.json"):
        self.path = Path(storage_path)

    def save_profile(self, name: str, profile: ClickProfile) -> None:
        data = self._load_all()
        data[name] = asdict(profile)
        self.path.write_text(json.dumps(data, indent=4))

    def get_profile(self, name: str) -> ClickProfile:
        data = self._load_all()
        if name not in data:
            raise ValueError(f"Profile {name} not found")
        return ClickProfile(**data[name])

    def _load_all(self) -> Dict[str, Any]:
        if not self.path.exists():
            return {}
        with open(self.path, "r") as f:
            return json.load(f)

    def delete_profile(self, name: str) -> None:
        data = self._load_all()
        if name in data:
            del data[name]
            self.path.write_text(json.dumps(data, indent=4))