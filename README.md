Изучил основы FastAPI и HTTP методы GET, POST, PUT, DELETE и их применение на практике.
Реализовал задание по теме 4 «Управление скидками в ритейле» — Promo & Discount Manager:
— GET /promos — список промокодов с фильтрацией по is_active и пагинацией
— GET /promos/{id} — получение промокода по ID с обработкой 404
— POST /promos — создание промокода со статусом 201
— PUT /promos/{id} — обновление (деактивация, изменение срока действия)
— DELETE /promos/{id} — удаление промокода со статусом 204
— POST /promos/apply — применение промокода к корзине с расчётом скидки и обработкой 400
Использовал Pydantic  для валидации входящих данных: ограничение discount_percent (1–90), принудительный перевод code в верхний регистр через @field_validator.
Подключил SQLAlchemy ORM с базой данных SQLite — реализовал полный CRUD слой (crud.py) с фильтрацией и пагинацией.
Проверил все эндпоинты через Swagger UI (/docs) и Postman — статус-коды 200, 201, 204, 400, 404 отрабатывают корректно.
# Promo Manager API

API для управления промокодами: создание, обновление, удаление и применение промокодов к корзине.

## Технологии

* Python 3.12
* FastAPI
* SQLAlchemy
* Pydantic v2
* Docker

## Запуск через Docker

```bash
git clone https://github.com/USERNAME/promo-manager.git
cd promo-manager
docker-compose up --build
```

Документация API будет доступна по адресу:

http://localhost:8000/docs

## Локальный запуск

```bash
git clone https://github.com/USERNAME/promo-manager.git
cd promo-manager
uv sync
uv run uvicorn main:app --reload
```

Документация API будет доступна по адресу:

http://127.0.0.1:8000/docs

## Эндпоинты

| Метод  | URL           | Описание                                            |
| ------ | ------------- | --------------------------------------------------- |
| GET    | /promos       | Получить список промокодов (фильтрация и пагинация) |
| GET    | /promos/{id}  | Получить промокод по ID                             |
| POST   | /promos       | Создать новый промокод                              |
| PUT    | /promos/{id}  | Обновить промокод или изменить срок действия        |
| DELETE | /promos/{id}  | Удалить промокод                                    |
| POST   | /promos/apply | Применить промокод к корзине                        |

<img width="2346" height="1436" alt="image" src="https://github.com/user-attachments/assets/e0569ae8-a190-4069-bd80-8c0b81ea50ed" />
