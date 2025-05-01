```plaintext
├── alembic.ini            # Alembic configuration
├── docker-compose.yml     # Docker Compose for PostgreSQL
├── requirements.txt       # Python dependencies
├── app
│   ├── main.py            # FastAPI application entrypoint
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic schemas
│   ├── crud.py            # CRUD operations
│   ├── dependencies.py    # DB/session and auth dependencies
│   ├── auth.py            # JWT/Auth handlers
│   └── alembic            # Migration scripts folder
└── tests
    └── test_main.py       # Pytest TestClient tests
```


. Технические требования
🔹 База данных
3 связанные таблицы (используйте SQLAlchemy + Pydantic)

Автоматическое создание SQLite-файла ИЛИ Docker с PostgreSQL

Миграции: Alembic (по желанию)

🔹 CRUD через FastAPI
Реализуйте эндпоинты POST, GET, PUT, DELETE для всех сущностей

🔹 Аутентификация и авторизация
Регистрация / Вход (JWT токены)

Как минимум 1 защищённый эндпоинт (например, просмотр задач только авторизованному пользователю)

🔹 Бизнес-логика (не CRUD!)
Примеры:

Алгоритм подсчёта рейтинга/приоритета

Подбор книг по интересам

Оптимизация расписания

Автоматическое распределение ресурсов и пр.

🔹 Тестирование
Используйте TestClient из FastAPI

Желательно покрытие pytest-тестами

Можно дополнительно подготовить коллекцию Postman