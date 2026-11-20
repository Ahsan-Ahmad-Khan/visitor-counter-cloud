from flask import Flask
import redis
import os

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True
)

@app.route("/")
def home():
    count = redis_client.incr("visitors")

    return f"""
    <html>
        <head>
            <title>Cloud Visitor Counter</title>
        </head>
        <body style="text-align:center; font-family:Arial; margin-top:100px;">
            <h1>Welcome to Cloud Visitor Counter</h1>
            <h2>Total Visitors: {count}</h2>
            <p>This application is powered by Flask and Redis.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)