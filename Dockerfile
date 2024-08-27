# Stage 1 - bundle base image

FROM python:3.12.3-alpine3.19 AS base

ENV \
  PYTHONFAULTHANDLER=TRUE \
  PYTHONUNBUFFERED=TRUE \
  POETRY_HOME="/opt/poetry" \
  POETRY_VIRTUALENVS_IN_PROJECT=true \
  POETRY_NO_INTERACTION=1 \
  PYSETUP_PATH="/opt/pysetup" \
  VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Stage 2 - build dependencies

FROM base AS builder

ARG POETRY_VERSION="1.8.2"

RUN pip install --upgrade pip && \
    pip install poetry==${POETRY_VERSION}

WORKDIR ${PYSETUP_PATH}

COPY pyproject.toml poetry.lock ./
RUN poetry install --only=main --no-root --no-interaction --no-ansi

COPY backend backend
COPY README.md README.md
RUN poetry install --only=main --no-interaction --no-ansi

# Stage 3 - build final runtime image

FROM base AS final

WORKDIR /app

EXPOSE 8080

COPY --from=builder $VENV_PATH $VENV_PATH

COPY backend backend

RUN python backend/manage.py migrate
RUN python backend/manage.py seed_db

CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8080"]
