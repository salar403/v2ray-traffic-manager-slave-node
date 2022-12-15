FROM python:3.10.5


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN curl -fsSL https://get.docker.com | sh
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY . .
