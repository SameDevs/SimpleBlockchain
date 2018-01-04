import os
import hashlib
import requests
import time
import json

from block import Block
from blockchain import Blockchain

from flask import Flask, request

app = Flask(__name__)

blockchain = Blockchain()
# A completely random address of the owner of this node
miner_address = "aaabbbcccd-random-miner-address-aaabbbcccd"

@app.route('/')
def hello():
    b = Block(0, time.ctime(), "Genesis Block", "0")
    return "%s, %s, %s, %s, %s" % (b.index, b.timestamp, b.data, b.hash, b.previous_hash)

@app.route('/blocks', methods=['GET'])
def getBlocks():
    return json.dumps(blockchain.getBlocksAsDictArray())

@app.route('/transactions', methods=['POST'])
def newTransaction():
    values = request.get_json()

    # Check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    return json.dumps(blockchain.addNewTransaction(values['sender'], values['recipient'], values['amount'])), 201

@app.route('/mine', methods=['GET'])
def mine():
    # Get the last proof of work
    # Find the proof of work for the current block being mined
    # Note: The program will hang here until a new proof of work is found
    proof = blockchain.proofOfWork()
    # Once we find a valid proof of work, we know we can mine a block so we reward the miner by adding a transaction
    blockchain.addNewTransaction("network", miner_address, 1)
    # Now we can gather the data needed to create the new block, empty transaction list, now create the new block!
    nBlock = blockchain.addNewBlockWithProof(proof)
    return json.dumps(nBlock.toDict())

if __name__ == "__main__":
    SERVICE_PORT = int(os.getenv("PORT", 5000))
    DEBUG_MODE = os.getenv("DEBUG", False)
    app.run(host="0.0.0.0", port=SERVICE_PORT, debug=DEBUG_MODE)
