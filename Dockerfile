FROM python:3.13-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /code

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        build-essential libpq-dev postgresql-client curl \
 && rm -rf /var/lib/apt/lists/*

COPY Pipfile* ./
RUN pip install --no-cache-dir pipenv \
 && pipenv install --deploy --system --ignore-pipfile


COPY . /code

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["gunicorn", "yclone.wsgi:application", "--bind", "0.0.0.0:8000"]
