import json
import os

def load_config(file_path, default_config):
    if not os.path.exists(file_path):
        return default_config
    with open(file_path, 'r') as config_file:
        config = json.load(config_file)
    return {**default_config, **config}

# Default configuration
DEFAULT_CONFIG = {
    'host': 'localhost',
    'port': 8080,
    'debug': False
}

# Load configuration from file
config = load_config('config.json', DEFAULT_CONFIG)