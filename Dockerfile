# Dockerfile
FROM python:3.12-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Default; Railway will inject $PORT at runtime
ENV PORT=5000

# Bind to 0.0.0.0 and Railway's $PORT
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:$PORT app:app"]
