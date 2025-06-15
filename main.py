from llama_cpp import Llama
from config import get_prompt, format_chat, MODEL_PATH
from history import write_history, read_history, print_history

print(Llama.__doc__)

def main():
    llm = Llama(
        model_path=MODEL_PATH,
        n_ctx=32768,
        n_threads=8,
        chat_format="chatml",
        verbose=False,
    )

    print("Модель загружена. ‘exit’ для выхода.")
    history = read_history()

    print_history(history)

    while True:
        user_input = input(">>> ").strip()
        if user_input.lower() in ("exit", "quit"):
            break

        prompt = format_chat(history, user_input)

        stream = llm(
            prompt,
            max_tokens=200,
            temperature=0.6,
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
