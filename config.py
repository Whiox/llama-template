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


def get_prompt():
    with open('prompt.txt', 'r', encoding='utf-8') as file:
        prompt = file.read()
    return prompt


def format_chat(history, user_input):
    prompt = get_prompt().strip()
    chat = "<|system|>\n" + prompt + "\n"

    for i, (u, a) in enumerate(history):
        if i > 0 and i % 5 == 0:
            chat += "<|system|>\n" + prompt + "\n"
        chat += f"<|user|>\n{u}\n<|assistant|>\n{a}\n"

    chat += "<|user|>\n" + user_input + "\n<|assistant|>\n"
    return chat


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

