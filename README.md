# 🧠 Habit Tracker API

Проект представляет собой backend-сервис для отслеживания полезных привычек. Пользователи могут создавать свои привычки,
получать напоминания через Telegram и управлять своим прогрессом.

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
SECRET_KEY=your-secret-key
DEBUG=True

POSTGRES_DB=habits_tracker
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your-password
DB_HOST=db
DB_PORT=5432

EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=465
EMAIL_HOST_USER=your-email
EMAIL_HOST_PASSWORD=your-password
EMAIL_USE_SSL=True

CELERY_BROKER_URL=redis://redis:6379/0
REDIS_URL=redis://redis:6379

CACHE_ENABLED=True

TELEGRAM_BOT_TOKEN=your-token
TELEGRAM_URL=https://api.telegram.org/bot
```

### 5. Применить миграции и создать суперпользователя:

```
python manage.py migrate
python manage.py createsuperuser
```

---

## 🐳 Запуск с помощью Docker

Проект полностью настроен для работы в Docker-контейнерах. Для работы потребуется
установленные [Docker](https://docs.docker.com/get-docker/)
и [Docker Compose](https://docs.docker.com/compose/install/).

### 1. Настройка переменных окружения

Создайте файл `.env` в корне проекта (на основе `.env.example`):

```bash
  cp .env.example .env
```

Заполните все необходимые переменные, особенно обратите внимание на:

env

### Для работы внутри Docker-сети

```
DB_HOST=db
CELERY_BROKER_URL=redis://redis:6379/0
REDIS_URL=redis://redis:6379
```

### 2. Сборка и запуск контейнеров

Запустите все сервисы одной командой:

```bash
  docker-compose up --build
```

Для запуска в фоновом режиме:

```bash
  docker-compose up -d --build
```

### 3. Сервисы и их порты

После запуска будут доступны:

```
Django приложение - http://localhost:8000

Admin панель - http://localhost:8000/admin

PostgreSQL - порт 5432 (внутри Docker-сети)

Redis - порт 6379 (внутри Docker-сети)
```

4. Полезные команды
   Просмотр логов:

```bash
  docker-compose logs -f  # всех сервисов
  docker-compose logs -f web  # только Django
```

Остановка контейнеров:

```bash
  docker-compose down
```

Применение миграций:

```bash
  docker-compose exec web python manage.py migrate
```

Создание суперпользователя:

```bash
  docker-compose exec web python manage.py createsuperuser
```

Запуск тестов:

```bash
  docker-compose exec web python manage.py test
```

### 5. Проверка работы Celery

Просмотр логов Celery worker:

```bash
  docker-compose logs -f celery
```

Просмотр логов Celery beat:

```bash
  docker-compose logs -f celery-beat
```

### 6. Очистка

Для полной очистки (включая volumes):

```bash
  docker-compose down -v
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