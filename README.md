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

REST API для управления промокодами на FastAPI + SQLAlchemy + Pydantic.

## Стек
- Python 3.11
- FastAPI
- SQLAlchemy (SQLite)
- Pydantic v2
- UV

## Установка и запуск

### 1. Установить зависимости
uv sync

### 2. Запустить сервер
uv run uvicorn main:app --reload

### 3. Открыть документацию
http://127.0.0.1:8000/docs

## Эндпоинты

| Метод  | URL                | Описание                        |
|--------|--------------------|---------------------------------|
| GET    | /promos            | Список промокодов (фильтр, пагинация) |
| GET    | /promos/{id}       | Получить по ID                  |
| POST   | /promos            | Создать промокод (статус 201)   |
| PUT    | /promos/{id}       | Обновить промокод               |
| DELETE | /promos/{id}       | Удалить промокод (статус 204)   |
| POST   | /promos/apply      | Применить промокод к корзине    |
<img width="2346" height="1436" alt="image" src="https://github.com/user-attachments/assets/e0569ae8-a190-4069-bd80-8c0b81ea50ed" />
