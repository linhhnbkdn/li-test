FROM python:3.12.4-slim-bookworm AS base

ARG ARG_USER_ID=1100
ARG ARG_GROUP_ID=1100
ENV USER_ID=${ARG_USER_ID}
ENV GROUP_ID=${ARG_GROUP_ID}


ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV LANG ja_JP.UTF-8
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN groupadd --system --gid $GROUP_ID app && \
    useradd --system --gid $GROUP_ID -m --uid $USER_ID app

ENV APP_DIR /app
WORKDIR $APP_DIR
RUN apt-get update && \
    apt-get upgrade -y

RUN apt-get install -y --no-install-recommends \
    locales \
    gcc \
    git \
    python3-dev libpq-dev \
    pkg-config \
    libcurl4-openssl-dev \
    libmagic1 \
    libssl-dev
RUN sed -i -e 's/# \(ja_JP.UTF-8\)/\1/' /etc/locale.gen && \
    locale-gen
RUN python -m pip install --upgrade pip
RUN python -m pip install pipenv
EXPOSE 4011

FROM base AS development
RUN apt-get install git -y
# COPY Pipfile Pipfile.lock ./
ENV PIPENV_VENV_IN_PROJECT=1
# ENTRYPOINT [ "pipenv", "run", "server" ]
