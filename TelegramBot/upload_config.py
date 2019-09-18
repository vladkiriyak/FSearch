import json


def get_config(path_to_config: str) -> dict:
    with open(path_to_config, "r") as config_file:
        config = json.load(config_file)
    return config


config: dict = get_config("/home/vlad/FSearch/TelegramBot/config.json")
