# Weather app
приложение, реализованное с помощью FastApi, где введя в URL /weather/<название города>, приложение вернет вам в JSON-формате информацию о погоде в городе.

## Установка

1. Клонируйте репозиторий с github (`git clone`)
2. Создайте виртуальное окружение (`python -m venv env`)
3. Установите зависимости `pip install -r requirements.txt`
4. Создайте файл `settings.py` в папке `setting_box`
5. Впишите в `settings.py` следующее:
```
API_KEY = 'Ваш API-ключ от openweathermap.org'
```
6. В командной строке запустите сервер (`uvicorn main:app --reload`)