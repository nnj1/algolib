class GraphNode():
    def __init__(self, content):
        self.content = content
    def setContent(self, content):
        self.content = content

class AdjacencyMatrix:
    def __init__(self):
        self.nodes = []
        self.mat = [[0]]
    def findNodeIndex(self, a):
        for i, node in enumerate(self.nodes):
            if a == node:
                return i
        return False
    def addNode(self, node):
        self.nodes.append(node)
        s = len(self.mat) + 1
        for row in self.mat:
            row.append(0)
        self.mat.append([0 for x in range(s)])
    def mark(self, x, y, l):
        i = self.nodes.index(x)
        j = self.nodes.index(y)
        self.mat[i][j] = l
        self.mat[j][i] = l
    def deleteNode(self, node):
        i = self.nodes.index(node)
        del self.mat[i]
        for row in mat:
            del row[i]
        self.nodes.remove(node)
    def printMatrix(self):
        # make sure to exlude the last row and column
        for row in self.mat[:-1]:
            print row[:-1]

class Graph:
    def __init__(self):
        self.matrix = AdjacencyMatrix()
    def adjacent(self, x, y):
        i = self.matrix.findNodeIndex(x)
        j = self.matrix.findNodeIndex(y)
        if self.matrix.mat[i][j] > 0 and self.matrix.mat[i][j] > 0:
            return True
        return False
    def neighbors(self, x):
        i = self.matrix.findNodeIndex(x)
        collection = []
        for k, item in enumerate(self.matrix.mat[i]):
            if item > 0:
                collection.append(self.matrix.nodes[k])
        return collection
    def addEdge(self, x, y, v = 1):
        self.matrix.mark(x, y, v)
    def getEdgeValue(self, x, y):
        i = self.matrix.findNodeIndex(x)
        j = self.matrix.findNodeIndex(y)
        if adjacent(x, y):
            return self.matrix.mat[i][j]
        return False
    def addNode(self, x):
        self.matrix.addNode(x)
    def addNodes(self, nodes):
        for node in nodes:
            self.matrix.addNode(node)
    def printAdjacencyMatrix(self):
        self.matrix.printMatrix()
        
# example
cities = Graph()

# create graph nodes
new_york = GraphNode('new york')
san_fran = GraphNode('san francisco')
tokyo = GraphNode('tokyo')
london = GraphNode('london')
france = GraphNode('france')

# load up nodes and edges
cities.addNodes([new_york, san_fran, tokyo, london, france])
cities.addEdge(new_york, tokyo, 4)
cities.addEdge(france, tokyo, 3)

# print the adjacency matrix
cities.printAdjacencyMatrix()

# test to see if two nodes are adjacent
print cities.adjacent(tokyo, france)

# find neighboring nodes
neighbors = cities.neighbors(tokyo)
for neighbor in neighbors:
    print neighbor.content
