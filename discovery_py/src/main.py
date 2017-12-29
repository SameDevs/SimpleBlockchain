import os
import json

from flask import Flask, request
from nodes_manager import NodesManager, Node

app = Flask(__name__)
NODES_MANAGER = NodesManager(app.logger)

@app.route('/nodes/register', methods=['POST'])
def register():
    node_port = int(request.args.get('port', 5000))
    new_node = Node(request.remote_addr, node_port)
    NODES_MANAGER.add_node(new_node)
    return json.dumps(NODES_MANAGER.get_nodes(new_node)), 201

@app.route('/nodes', methods=['GET'])
def list_nodes():
    node_port = int(request.args.get('port', 5000))
    current_node = Node(request.remote_addr, node_port)
    return json.dumps(NODES_MANAGER.get_nodes(current_node))

if __name__ == "__main__":
    SERVICE_PORT = int(os.getenv("PORT", 5000))
    DEBUG_MODE = os.getenv("DEBUG", False)
    app.run(host="0.0.0.0", port=SERVICE_PORT, debug=DEBUG_MODE)
