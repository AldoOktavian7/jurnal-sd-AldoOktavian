# STAGE 1: Builder
FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user -r requirements.txt

# STAGE 2: Production (Final)
FROM python:3.9-alpine

WORKDIR /app

COPY --from=builder /root/.local /root/.local

COPY . .

ENV APP_USER="Developer Mahasiswa"
ENV APP_ENV="development"
ENV PYTHONUNBUFFERED=1

ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000

CMD ["python", "app.py"]