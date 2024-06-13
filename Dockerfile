FROM python:3.11.0-slim

WORKDIR /bg2b_v2

COPY ./reqirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip isntall gunicorn

ENTRYPOINT []