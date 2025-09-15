from flask import Flask, jsonify
import os, redis

def make_client():
    # Railway’s Redis exposes REDIS_URL (and also REDISHOST/REDISPORT/REDISPASSWORD)
    url = os.getenv("REDIS_URL")
    if url:
        return redis.from_url(url, decode_responses=True)
    return redis.Redis(
        host=os.getenv("REDIS_HOST", os.getenv("REDISHOST", "localhost")),
        port=int(os.getenv("REDIS_PORT", os.getenv("REDISPORT", 6379))),
        password=os.getenv("REDIS_PASSWORD", os.getenv("REDISPASSWORD")),
        decode_responses=True,
    )

r = make_client()
app = Flask(__name__)

@app.route("/")
def hello():
    count = r.incr("page_views")
    return f"Hello from Flask + Redis! Views: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
