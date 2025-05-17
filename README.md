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
- 🌐 Проксирование через Nginx
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
- Nginx

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

Создайте файл `.env` в корне проекта (на основе `.env_sample`):

```bash
  cp .env_sample .env
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


## 🚀 Деплой на сервер с Docker и Nginx

### 🔧 1. Установи зависимости на сервер

На сервере должны быть установлены:
```
•	Docker
•	docker-compose
•	доступ по SSH
```

### 📦 2. Клонируй репозиторий на сервер
```
git clone https://github.com/LeojBang/habits-tracker-drf.git
cd habits-tracker-drf
```
### ⚙️ 3. Создай .env файл
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

### 🐳 4. Собери и запусти контейнеры
```bash
   docker-compose build
   docker-compose up -d
```

### ✅ 5. Проверка
Открой в браузере:
```
http://your-server-ip/
```
Если всё работает — увидишь главную страницу Django или /admin/.

### 🌐 6. Nginx — настройка
Проект уже содержит рабочий конфиг nginx.conf. Он:
```
• проксирует запросы на backend Django (контейнер web)
• отдаёт статику из volume /app/staticfiles
```
### 📁 nginx/nginx.conf
Пример содержимого:
```
events {
    worker_connections 1024;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    upstream django {
        server web:8000;
    }

    server {
        listen 80;
        server_name _;

        location /static/ {
            alias /app/staticfiles/;
        }

        location / {
            proxy_pass http://django;
        }
    }
}
```

### 🧹 7. Обновление проекта
При внесении изменений:
```bash
   git pull origin main
   docker-compose down
   docker-compose build
   docker-compose up -d
```

## ⚙️ CI/CD: Деплой с GitHub Actions

Проект включает автоматизированный деплой на сервер при пуше в ветку main с помощью GitHub Actions.

🔐 2. Секреты: проверь, что они добавлены в GitHub → Settings → Secrets → Actions

	•	SECRET_KEY
	•	DOCKER_HUB_ACCESS_TOKEN
	•	DOCKER_HUB_USERNAME
	•	SSH_KEY (закрытый ключ в PEM-формате)
	•	SSH_USER
	•	SERVER_IP
### 📌 Закрытый ключ можно получить командой:
```bash
  cat ~/.ssh/id_ed25519
```

### ✅ Команды на сервере (однократно перед первым деплоем):
```
# Установить Docker и docker-compose
# Затем:
git clone git@github.com:your-username/habits-tracker-drf.git
cd habits-tracker-drf
touch .env  # и заполнить переменные
```
### ✅ Как это работает
	1. При push или pull request запускается:
	  • линтер flake8
	  • тесты через manage.py test
	  • сборка Docker-образа и отправка в Docker Hub
	2. Если это push в ветку main, запускается деплой:
	  • GitHub Actions подключается к серверу по SSH
	  • Обновляет код и пересобирает проект через docker-compose