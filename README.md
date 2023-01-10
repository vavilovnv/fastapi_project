## Шаблон fastapi проекта

### Установка и запуск

1. Клонировать репозитарий:
```
git clone https://github.com/vavilovnv/fastapi_project
```

2. Установить все зависимости:
```
pip install -r requirements.txt
```
3. Запустить контейнер "postgres-fastapi":
```
docker run \
  --rm   \
  --name postgres-fastapi \
  -p 5532:5432 \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=collection \
  -d postgres:14.5 
```
4. Создать миграции:
```
alembic revision --autogenerate -m 01_initial-db
```
5. Выполнить миграции:
```
alembic upgrade head
```
6. Запустить на исполнение main.py
```
python3 ./src/main.py
```
7. Открыть страницу документации (http://0.0.0.0:8000/api/openapi) и проверить методы CRUD.