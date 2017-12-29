import os
import hashlib
import requests
import time

from block import Block

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    b = Block(0, time.ctime(), "Genesis Block", "0")
    return "%s, %s, %s, %s, %s" % (b.index, b.timestamp, b.data, b.hash, b.previous_hash)


if __name__ == "__main__":
    SERVICE_PORT = int(os.getenv("PORT", 5000))
    DEBUG_MODE = os.getenv("DEBUG", False)
    app.run(host="0.0.0.0", port=SERVICE_PORT, debug=DEBUG_MODE)
