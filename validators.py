import re

class ClickValidator:
    @staticmethod
    def is_valid_interval(interval: float) -> bool:
        return isinstance(interval, (int, float)) and interval >= 0.01

    @staticmethod
    def is_valid_coordinate(coord: int) -> bool:
        return isinstance(coord, int) and coord >= 0

    @staticmethod
    def is_valid_button(button: str) -> bool:
        return button in {'left', 'right', 'middle'}

    @staticmethod
    def validate_config(config: dict) -> bool:
        required = {'interval', 'button', 'x', 'y'}
        if not all(k in config for k in required):
            return False
        
        return (
            ClickValidator.is_valid_interval(config['interval']) and
            ClickValidator.is_valid_button(config['button']) and
            ClickValidator.is_valid_coordinate(config['x']) and
            ClickValidator.is_valid_coordinate(config['y'])
        )

class KeyValidator:
    @staticmethod
    def is_valid_key(key: str) -> bool:
        return bool(re.match(r'^[a-z0-9_]{1,10}$', key))