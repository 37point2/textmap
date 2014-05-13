class Node():
    def __init__(self):
        self.name
        self.edges = {}
        self.tags = []

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def addEdge(self, edge):
        try:
            self.edges[edge] += 1
        except:
            self.edges[edge] = 1
                
    def getEdges(self):
        return self.edges
    
    def addTag(self, tag):
        try:
            self.tags[tag] += 1
        except:
            self.tags[tag] = 1
                
    def getTags(self):
        return self.tags