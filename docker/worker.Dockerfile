FROM python:3.12-slim
WORKDIR /app
COPY backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY backend /app/backend
COPY workers /app/workers
WORKDIR /app/workers
ENV PYTHONPATH=/app/backend
CMD ["celery", "-A", "celery_app.celery_app", "worker", "--loglevel=info"]
