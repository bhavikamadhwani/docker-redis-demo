from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis. The hostname 'redis' is the name of the service we'll define in Docker Compose.
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    # Increment the visit count and get the new value
    count = redis_client.incr('page_views')
    return f"Hello from Docker on Windows! This page has been viewed {count} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)