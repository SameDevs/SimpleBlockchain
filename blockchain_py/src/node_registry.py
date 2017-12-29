class NodeRegistry__:
    def __init__(self):
        self.node_list = []

    def update_list(self, node_list):
        self.node_list = node_list

    def get_list(self):
        return self.node_list


class NodeRegistry:
    instance__ = None

    @staticmethod
    def instance():
        if NodeRegistry.instance__ is None:
            NodeRegistry.instance__ = NodeRegistry__()
        return NodeRegistry.instance__
