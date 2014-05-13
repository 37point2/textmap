import node

class Graph():
    def __init__(self):
        self.name_index = {}
        self.nodes = []

    def getOrAddNode(self, name):
        if not self.name_index.has_key(name):
            _node = node()
            _node.setName(name)
            self.nodes.append(_node)
            self.name_index[name] = self.nodes.index(_node)
        else:
            _node = self.nodes[self.name_index[name]]
            return _node

    def addNode(self, name):
        _node = node()
        _node.setName(name)
        self.nodes.append(_node)
        self.name_index[name] = self.nodes.index(_node)

    def updateEdges(self, _node, name):
        if self.name_index.has_key(name):
            index = self.name_index[name]
            _node.addEdge(index)
        else:
            self.addNode(name)
            index = self.name_index[name]
            _node.addEdge(index)

    def getNodes(self):
        return self.nodes

    def getIndex(self):
        return self.name_index