import json

def write_history(history, filename='history.json') -> None:
    data = [{"user": u, "assistant": a} for u, a in history]

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def read_history(filename='history.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [(item["user"], item["assistant"]) for item in data]
    except FileNotFoundError:
        return []


def print_history(history):
    if not history:
        return

    for i, (user_msg, assistant_msg) in enumerate(history, start=1):
        print(f">>> {user_msg}")
        print(f"{assistant_msg}")
        print()
