import io
import json
import os


DEFAULT_CONFIG = {
    "model": {
        "filename": "none.gguf"
    }
}


def create_config(func):
    def wrapper(*args, **kwargs):
        try:
            with open("config.json", "r") as file:
                config = json.load(file)
                return func(*args, **kwargs)
        except FileNotFoundError:
            with open("config.json", "w") as file:
                file.write(json.dumps(DEFAULT_CONFIG, indent=2))
                return func(*args, **kwargs)

    return wrapper


@create_config
def get_model_path():
    with open('config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
    return f"models/{config['model']['filename']}"


@create_config
def find_models():
    models = []
    for file in os.listdir("models"):
        if file.endswith(".gguf"):
            models.append(file)
    return models


@create_config
def write_models(model):
    print(model)
    with open("config.json", "r") as file:
        config = json.load(file)

    config["model"]["filename"] = model

    with open("config.json", "w") as file:
        json.dump(config, file, indent=2)

