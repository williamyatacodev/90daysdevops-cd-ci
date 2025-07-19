FROM python:3.12-slim AS base
LABEL author="williamyatacodev"

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/app

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

FROM base AS dev

ENV FLASK_ENV=development

CMD ["python", "app.py"]

FROM base AS final

COPY . .

EXPOSE 80

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80"]
