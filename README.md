# 🧠 Habit Tracker API

Проект представляет собой backend-сервис для отслеживания полезных привычек. Пользователи могут создавать свои привычки, получать напоминания через Telegram и управлять своим прогрессом.

---

## 🚀 Возможности

- 📌 Создание и управление привычками
- 🔁 Периодические напоминания через Telegram
- 🌍 Публичные привычки (доступны всем пользователям)
- 🔒 Аутентификация и авторизация
- ⚙️ Отложенные задачи через Celery
- 📄 Валидация правил привычек
- 🔄 Пагинация
- 🔐 CORS-конфигурация
- Работа с переменными окружения через `.env`


---
## 🛠 Технологии

- Python 3.10+
- Django 4+
- Django REST Framework
- Celery + Redis
- Telegram Bot API
- requests, pytz
- django-cors-headers

## 📂 Установка и запуск

### 1. Клонировать репозиторий

```bash
  git clone https://github.com/LeojBang/habits-tracker-drf.git
```

### 2. Создать и активировать виртуальное окружение
```bash
    python -m venv venv
    source venv/bin/activate  
```
```bash
    Windows: venv\Scripts\activate
```
### 3. Установить зависимости
```bash
    pip install -r requirements.txt
```

### 4. Настроить переменные окружения:
Создайте файл .env:
```
SECRET_KEY=
DEBUG=

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=465
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_SSL=True

CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

CACHE_ENABLED=True
REDIS_URL=redis://127.0.0.1:6379

TELEGRAM_BOT_TOKEN=
TELEGRAM_URL=https://api.telegram.org/bot
```
### 5. Применить миграции и создать суперпользователя:
```
python manage.py migrate
python manage.py createsuperuser
```

### 6. Запустить сервер:
```bash
  python manage.py runserver
```

### 7. Запустить воркер Celery:
```bash
  celery -A config worker --loglevel=info
```

### 8. Тестирование:
Запустить тесты и узнать результат покрытия
```bash
  coverage run --source='.' manage.py test
```
```bash
  coverage report -m
```