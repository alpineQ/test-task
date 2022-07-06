## Тестовое задание
### Требования к запуску
- Файл `credentials.json` в папке проекта с полученный в Google Cloud расположенный в корне проекта
### Запуск
Обычный запуск:
``` bash
# При запуске на Ubuntu/Debian подобных дистрибутивах
sudo apt install python3 python3-pip
python3 -m pip install -r requirements.txt
python3 main.py
```
Запуск в виртуальном окружении:
``` bash
# При запуске на Ubuntu/Debian подобных дистрибутивах
sudo apt install python3 python3-pip
python3 -m pip install virtualenv
venv venv
python3 -m pip install -r requirements.txt
python3 main.py
```
