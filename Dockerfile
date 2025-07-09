FROM python:3.13-slim

WORKDIR /code

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        postgresql-client \
        curl \
 && rm -rf /var/lib/apt/lists/*

COPY Pipfile* /code/
RUN pip install --no-cache-dir pipenv \
 && pipenv install --deploy --system --ignore-pipfile --dev

COPY . /code
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["./entrypoint.sh"]