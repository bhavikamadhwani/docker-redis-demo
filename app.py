from flask import Flask
import os
import redis

app = Flask(__name__)

# Function to create Redis client - PRIORITIZE Railway's REDIS_URL
def make_client():
    # Railway’s Redis exposes REDIS_URL (and also REDISHOST/REDISPORT/REDISPASSWORD)
    url = os.getenv("REDIS_URL")
    if url:
        return redis.from_url(url, decode_responses=True)
    return redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        password=os.getenv("REDIS_PASSWORD", ""),
        decode_responses=True,
    )

# Initialize Redis client
r = make_client()

@app.route("/")
def hello():
    try:
        count = r.incr("page_views")
        return f"Hello from Flask + Redis on Railway! Views: {count}"
    except redis.exceptions.ConnectionError:
        return "Temporarily unable to connect to Redis.", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
