FROM python:3.10.5-slim

WORKDIR /app
RUN apt-get update && apt-get -y install libpq-dev gcc

COPY pyproject.toml ./
RUN python -m pip install --no-cache-dir --upgrade pip
RUN pip install poetry
RUN poetry install
COPY planty/ ./planty
EXPOSE 8000
