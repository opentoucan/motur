ARG PYTHON_SLIM=docker.io/python:3.14
FROM ${PYTHON_SLIM} AS builder
ARG USERNAME=app
ARG USER_UID=2048
ARG USER_GID=$USER_UID

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    apt-transport-https \
    gcc \
    libc6 \
    libgl1 \
    libglib2.0-0 \
    git \
    curl \
    wget \
    jq \
    chromium

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev --no-editable


ADD . /app

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-editable

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

USER $USERNAME
ENTRYPOINT ["/app/.venv/bin/fastapi", "run", "src/main.py", "--port", "8080", "--host", "0.0.0.0"]
