class GraphNode():
    def __init__(self, content):
        self.content = content
    def setContent(self, content):
        self.content = content

class AdjacencyMatrix:
    def __init__(self):
        self.nodes = []
        self.mat = [[0]]
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
        self.mat.del(i)
        for row in mat:
            row.del(i)
        self.nodes.remove(node)
    def printMatrix(self):
        for row in self.mat:
            print row

class Graph:
    def __init__(self):
        self.matrix = AdjacencyMatrix()
    def adjacent(self, x, y):
        pass
    def neighbors(self, x, y):
        pass
    def addEdge(self, x, y, v = 1):
        self.matrix.mark(x, y, v)
    def addNode(self, x):
        self.matrix.addNode(x)
    def addNodes(self, nodes):
        for node in nodes:
            self.matrix.addNode(node)
    def printAdjacencyMatrix(self):
        self.matrix.printMatrix()
        
# example
cities = Graph()

new_york = GraphNode('new york')
san_fran = GraphNode('san francisco')
tokyo = GraphNode('meow')
london = GraphNode('rubbish')

cities.addNodes([new_york, san_fran, tokyo, london])
cities.addEdge(new_york, tokyo, 4)
cities.printAdjacencyMatrix()
