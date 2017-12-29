import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!!!'


if __name__ == "__main__":
    SERVICE_PORT = int(os.getenv("PORT"))
    DEBUG_MODE = os.getenv("DEBUG", False)
    app.run(host="0.0.0.0", port=SERVICE_PORT, debug=DEBUG_MODE)
