import os
import json

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def write_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def list_files_in_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def get_file_extension(file_name):
    return os.path.splitext(file_name)[1]
