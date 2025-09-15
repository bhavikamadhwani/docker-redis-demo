from flask import Flask
import redis
import os

app = Flask(__name__)

# Get the Redis host from an environment variable, default to 'redis' for local development
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_client = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def hello():
    try:
        count = redis_client.incr('page_views')
        return f"Hello from Docker on Windows! This page has been viewed {count} times."
    except redis.exceptions.ConnectionError:
        return "Could not connect to Redis. Please try again later.", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
