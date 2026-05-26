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