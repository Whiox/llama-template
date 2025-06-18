
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


def format_chat(history, user_input, max_tokens=32000):
    system_prompt = "<|system|>\n" + get_prompt().strip() + "\n"

    chat_body = ""
    for u, a in history:
        chat_body += f"<|user|>\n{u}\n<|assistant|>\n{a}\n"
    chat_body += f"<|user|>\n{user_input}\n<|assistant|>\n"

    full_prompt = system_prompt + chat_body
    trimmed_history = history[:]
    while len(full_prompt.split()) > max_tokens and trimmed_history:
        trimmed_history.pop(0)
        chat_body = ""
        for u, a in trimmed_history:
            chat_body += f"<|user|>\n{u}\n<|assistant|>\n{a}\n"
        chat_body += f"<|user|>\n{user_input}\n<|assistant|>\n"
        full_prompt = system_prompt + chat_body

    return full_prompt
