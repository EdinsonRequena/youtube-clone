# YClone

## .env

```dotenv
# Django
DJANGO_ENV=local
SECRET_KEY="django-insecure-bju*6e0-by@f9o02spa*b342!h0c2pb$r#6_g=tn8$n%4@(08%"
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# DB
POSTGRES_DB=yclone
POSTGRES_USER=yclone
POSTGRES_PASSWORD=yclone
DB_HOST=db
DB_URL=postgres://yclone:yclone@db:5432/yclone
```

## Arranque rápido

```bash
docker compose up --build -d
open http://localhost
```

## Tests

```bash
docker compose exec web pytest -q
```

