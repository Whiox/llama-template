from llama_cpp import Llama
from config import get_prompt, format_chat, get_model_path, find_models, write_models
from history import write_history, read_history, print_history, delete_history

print(Llama.__doc__)

def main():
    while True:
        try:
            llm = Llama(
                model_path=get_model_path(),
                n_ctx=32768,
                n_threads=8,
                chat_format="chatml",
                verbose=False,
            )
            break
        except ValueError:
            print(f"Модель по пути {get_model_path()} не найдена\n"
                  f"Для использования модели поместите её в папку models\n"
                  f"После добавьте полное название файла в config.json\n\n"
                  f"Или выберете из списка моделей:")
            models = find_models()

            for index, model in enumerate(models):
                print(f"{index}) {model}")

            write_models(models[int(input("Введите номер модели: "))])

    print("Модель загружена. ‘exit’ для выхода, clear для очистки истории.")
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

        prompt = format_chat(history, user_input)

        stream = llm(
            prompt,
            max_tokens=200,
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
