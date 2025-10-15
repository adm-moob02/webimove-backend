FROM python:3.13-slim AS base

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /backend

COPY ./backend ./pyproject.toml ./uv.lock /backend/

ENTRYPOINT [ "uv" ]

FROM base AS local

RUN uv sync --all-groups && uv venv

CMD [ "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload" ]

FROM base AS prod

RUN uv sync

CMD [ "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
