import os
import json
import requests

from flask import Flask, request

nodes = []

app = Flask(__name__)

def get_nodes(node_addr):
    res_nodes = []
    other_nodes = [n for n in nodes if n != node_addr]

    # Check nodes health
    for node in other_nodes:
        try:
            requests.get(f'http://{node}:{int(os.getenv("PORT", 5000))}/node/check')
            res_nodes.append(nodes)
        except Exception:
            # Nodes did not responded, remove from global nodes list
            nodes.remove(node)

    return res_nodes

def notify_all_nodes(new_node_addr):
    other_nodes = [n for n in nodes if n != new_node_addr]

    # Send new node address to other nodes
    for node in other_nodes:
        app.logger.info('Sending new node address to %s', node)
        try:
            requests.post(f'http://{node}:{int(os.getenv("PORT", 5000))}/node/update', data={ 'newNodeAddress': new_node_addr })
        except Exception:
            # Nodes did not responded, remove from global nodes list
            nodes.remove(node)

@app.route('/nodes/register', methods=['POST'])
def register():
    new_node_addr = request.remote_addr
    if new_node_addr not in nodes:
        app.logger.info('New node registered: %s', new_node_addr)
        nodes.append(new_node_addr)

        notify_all_nodes(new_node_addr)

    return json.dumps(get_nodes(new_node_addr)), 201

@app.route('/nodes', methods=['GET'])
def list_nodes():
    node_addr = request.remote_addr
    app.logger.info('Node list: %s', nodes)
    return json.dumps(get_nodes(node_addr))

if __name__ == "__main__":
    SERVICE_PORT = int(os.getenv("PORT", 5000))
    DEBUG_MODE = os.getenv("DEBUG", False)
    app.run(host="0.0.0.0", port=SERVICE_PORT, debug=DEBUG_MODE)
