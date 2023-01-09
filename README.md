## Шаблон fastapi проекта

### How to install

```
git clone https://github.com/vavilovnv/fastapi_project

pip install -r requirements.txt

docker run \
  --rm   \
  --name postgres-fastapi \
  -p 5532:5532 \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=collection \
  -d postgres:14.5 
```