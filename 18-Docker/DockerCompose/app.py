from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis
redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)


@app.route("/")
def hello():
    count = redis_client.incr("count")

    return f"Hello from Flask! You have visited this page {count} times."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)