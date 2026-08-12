import json
import os

DEFAULT_CONFIG = {
    'click_interval': 0.1,
    'click_duration': 10,
    'click_count': 100,
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = {**DEFAULT_CONFIG}
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)