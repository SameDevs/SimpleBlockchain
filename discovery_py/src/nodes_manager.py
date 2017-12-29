import json
import requests

class Node():
    """Class used to describe a node registered into this cluster"""
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __eq__(self, other):
        return self.host == other.host and self.port == other.port
 
    def __ne__(self, other):
        return self.host != other.host or self.port != other.port

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '%s:%s' % (self.host, self.port)

class NodesManager:
    def __init__(self, logger):
        self.logger = logger
        self.nodes = []

    def get_nodes(self, node):
        self.logger.info('Node list: %s', self.nodes)

        res_nodes = []
        other_nodes = [n for n in self.nodes if n != node]

        # Check nodes health
        for node in other_nodes:
            self.logger.info('Checking node status for %s', node)
            try:
                requests.get(f'http://{node.host}:{node.port}/node/check')
                res_nodes.append(str(node))
            except Exception:
                # Nodes did not respond, remove from global nodes list
                self.logger.info('Node %s is NOT ACTIVE', node)
                self.nodes.remove(node)

        return res_nodes

    def add_node(self, new_node):
      if new_node not in self.nodes:
        self.logger.info('New node registered: %s', new_node)
        self.nodes.append(new_node)

        self.__notify_all_nodes__(new_node)

    def __notify_all_nodes__(self, new_node):
        other_nodes = [n for n in self.nodes if n != new_node]

        # Send new node address to other nodes
        for node in other_nodes:
            self.logger.info('Sending new node address to %s', node)
            try:
                requests.post(f'http://{node.host}:{node.port}/node/update', json=json.dumps(self.get_nodes(node)))
            except Exception:
                # Nodes did not responded, remove from global nodes list
                self.nodes.remove(node)
