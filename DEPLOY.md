# Развёртывание на Render

В настройках существующего Web Service выберите этот репозиторий, ветку
`main` и окружение Python. Поле Root Directory оставьте пустым.

- Build Command: `pip install -r requirements.txt`
- Start Command: `python 05-example_bot/bot.py`
- Environment: добавьте `GOOGLE_API_KEY` для Gemini.
- Для хранения заявок между перезапусками добавьте `DATABASE_URL` с адресом
  PostgreSQL. Без неё приложение пишет заявки в локальный `leads.json`.

Приложение слушает `0.0.0.0` и берёт порт из переменной `PORT` Render.
После деплоя откройте адрес сервиса и спросите, например, сколько стоит стрижка.
