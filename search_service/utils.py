import json


def get_config(path_to_config: str) -> dict:
    with open(path_to_config) as config_file:
        config = json.load(config_file)
    return config
