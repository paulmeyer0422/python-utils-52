import json

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.user_config = {}

    def load(self, config_file):
        try:
            with open(config_file, 'r') as file:
                self.user_config = json.load(file)
        except FileNotFoundError:
            self.user_config = {}
        except json.JSONDecodeError:
            self.user_config = {}

    def get_config(self):
        return {**self.default_config, **self.user_config}

if __name__ == '__main__':
    default_settings = {'click_interval': 0.1, 'duration': 60}
    config_loader = ConfigLoader(default_settings)
    config_loader.load('config.json')
    config = config_loader.get_config()
    print(config)