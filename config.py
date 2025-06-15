import json


def get_prompt():
    with open('prompt.txt', 'r', encoding='utf-8') as file:
        prompt = file.read()
    return prompt


def format_chat(history, user_input):
    chat = "<|system|>\n" + get_prompt().strip() + "\n"
    for u, a in history:
        chat += f"<|user|>\n{u}\n<|assistant|>\n{a}\n"
    chat += f"<|user|>\n{user_input}\n<|assistant|>\n"
    return chat


def get_model_path():
    with open('config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
    return f"models/{config['model']['filename']}"
