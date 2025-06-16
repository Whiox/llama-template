import json


def create_history(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            with open('history.json', 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=4)
            return func(*args, **kwargs)
    return wrapper


@create_history
def write_history(history, filename='history.json') -> None:
    data = [{"user": u, "assistant": a} for u, a in history]

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@create_history
def read_history(filename='history.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [(item["user"], item["assistant"]) for item in data]


@create_history
def delete_history(filename='history.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump([], f, ensure_ascii=False, indent=2)


def print_history(history):
    if not history:
        return

    for i, (user_msg, assistant_msg) in enumerate(history, start=1):
        print(f">>> {user_msg}")
        print(f"{assistant_msg}")
        print()
