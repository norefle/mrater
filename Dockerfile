FROM python:3.7-alpine

RUN apk add dumb-init

# Configure
ENV POETRY_VERSION=0.12.17
RUN pip install "poetry==$POETRY_VERSION"

# Install dependencies
COPY poetry.lock pyproject.toml /app/

# Install app
COPY . /app

WORKDIR /app

RUN poetry config settings.virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

# Run

EXPOSE 8080

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080", "--workers", "2"]
