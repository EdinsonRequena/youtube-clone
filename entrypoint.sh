#!/usr/bin/env bash
set -e

echo "Waiting for PostgreSQL to be ready…"
until pg_isready -h "$DB_HOST" -p 5432 -U "$POSTGRES_USER" >/dev/null 2>&1; do
  sleep 1
done
echo "PostgreSQL is available"

echo "Running migrations"
python manage.py migrate --noinput

echo "📦 Collecting static files"
python manage.py collectstatic --noinput --clear

echo "Starting Gunicorn"
exec gunicorn yclone.wsgi:application \
      --bind 0.0.0.0:8000 \
      --workers 3 \
      --timeout 90