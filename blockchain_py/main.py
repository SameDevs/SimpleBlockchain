import os
import hashlib
import requests

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return hashlib.sha256('Hello World!!!'.encode()).hexdigest()


if __name__ == "__main__":
    SERVICE_PORT = int(os.getenv("PORT", 5000))
    DEBUG_MODE = os.getenv("DEBUG", False)
    app.run(host="0.0.0.0", port=SERVICE_PORT, debug=DEBUG_MODE)
