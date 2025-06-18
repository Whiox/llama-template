from llama_cpp import Llama
from config import get_model_path, change_model, get_config
from history import write_history, read_history, print_history, delete_history
from model import format_chat

print(Llama.__doc__)

def main():
    while True:
        try:
            config = get_config()

            llm = Llama(
                model_path=get_model_path(),
                n_ctx=config['n_ctx'],
                n_threads=config['n_threads'],
                chat_format="chatml",
                verbose=False,
            )
            break
        except ValueError:
            print(f"Модель по пути {get_model_path()} не найдена\n"
                  f"Для использования модели поместите её в папку models\n"
                  f"После добавьте полное название файла в config.json\n\n"
                  f"Или выберете из списка моделей:")

            change_model()

    print("Модель загружена. ‘exit’ для выхода, clear для очистки истории. change для смены модели")
    history = read_history()

    print_history(history)

    while True:
        user_input = input(">>> ").strip()
        if user_input.lower() in ("exit", "quit"):
            break
        elif user_input.lower() == "clear":
            delete_history()
            history = read_history()
            continue
        elif user_input.lower() == "change":
            change_model()
            continue

        prompt = format_chat(history, user_input)

        stream = llm(
            prompt,
            max_tokens=800,
            temperature=0.8,
            top_p=0.9,
            repeat_penalty=1.2,
            stream=True,
            stop=["<|user|>", "<|assistant|>"],
        )

        reply = ""
        for chunk in stream:
            text = chunk["choices"][0].get("text", "")
            text = text.lstrip("\n")
            print(text, end="", flush=True)
            reply += text

        reply = reply.rstrip("\n")
        print()

        history.append((user_input, reply))

        write_history(history)


if __name__ == "__main__":
    main()
