
## Мой шаблон под взаимодействие с моделями машинного обучения (.gguf) при помощи llama-cpp

### Установка и использование

#### Установка

##### Убедитесь, у вас установлены следующие программы:

- [Visual Studio](https://visualstudio.microsoft.com/ru/visual-cpp-build-tools/) с инструментами сборки C++
- [cmake](https://cmake.org/download/)
- [git](https://git-scm.com/downloads)
- [python](https://www.python.org/downloads/) 3.10 и выше

##### Клонируйте репозиторий

```bash
git clone https://github.com/Whiox/llama-template.git
```

##### Установите зависимости (загрузка может занять много времени)

```bash
pip install -r requirements.txt
```

Загрузите модель .gguf в папку models

Запустите main.py, выберите нужную модель

Доступны команды: exit, clear (очистка истории), swap (изменить модель)
