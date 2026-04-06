# django_sprint4

# Blogicum

Блог-платформа на Django, где пользователи могут публиковать посты, оставлять комментарии и управлять своим профилем.

## Технологии

- Python 3.x
- Django 3.2.16
- django-bootstrap5
- Pillow
- pytest

## Установка и запуск

### 1. Клонировать репозиторий
```bash
git clone https://github.com/nxnamee/django_sprint4.git
cd django_sprint4
```

### 2. Создать и активировать виртуальное окружение
```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

### 4. Применить миграции
```bash
cd blogicum
python manage.py migrate
```

### 5. Загрузить тестовые данные (опционально)
```bash
python manage.py loaddata ../db.json
```

### 6. Запустить сервер
```bash
python manage.py runserver
```

Проект будет доступен по адресу: http://127.0.0.1:8000/

## Основные команды

| Команда | Описание |
|--------|----------|
| `python manage.py runserver` | Запуск сервера разработки |
| `python manage.py migrate` | Применение миграций |
| `python manage.py makemigrations` | Создание новых миграций |
| `python manage.py createsuperuser` | Создание администратора |
| `python manage.py loaddata ../db.json` | Загрузка тестовых данных |

## Запуск тестов
```bash
cd ..  # вернуться в корень проекта
pytest
```

## Админ-панель

После создания суперпользователя админ-панель доступна по адресу:
http://127.0.0.1:8000/admin/

## Структура проекта
```
django_sprint4/
├── blogicum/          # Основной Django-проект
│   ├── blog/          # Приложение блога (посты, комментарии)
│   ├── pages/         # Статические страницы (о проекте, правила)
│   ├── templates/     # HTML-шаблоны
│   └── static/        # Статические файлы (CSS, изображения)
├── tests/             # Тесты
├── requirements.txt   # Зависимости
└── db.json            # Фикстуры с тестовыми данными
```