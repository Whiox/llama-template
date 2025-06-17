
DEFAULT_PROMPT = """
Ты - ассистент, говорящий только на русском. 
Твоя задача - показать пользователю всё, на что ты способен.
"""


def create_prompt(func):
    def wrapper(*args, **kwargs):
        try:
            with open('prompt.txt', 'r', encoding='utf-8') as file:
                prompt = file.read()
                return func(*args, **kwargs)
        except FileNotFoundError:
            with open('prompt.txt', 'w', encoding='utf-8') as file:
                file.write(DEFAULT_PROMPT)
                return func(*args, **kwargs)
    return wrapper


@create_prompt
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
