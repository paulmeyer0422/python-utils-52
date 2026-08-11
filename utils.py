def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

def chunk_list(data, chunk_size):
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

from collections import defaultdict

def group_by(data, key_func):
    grouped = defaultdict(list)
    for item in data:
        key = key_func(item)
        grouped[key].append(item)
    return dict(grouped)

import json

def save_to_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def load_from_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)