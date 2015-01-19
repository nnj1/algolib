class BinaryNode:
    def __init__(self, value, thing = None):
        self.value = value
        self.content = []
        self.content.append(thing)
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.duplicates = []
    def addLeftChild(self, node):
        self.leftChild = node
    def addRightChild(self, node):
        self.rightChild = node
    def addDuplicate(self, node):
        self.duplicates.append(node)
    
class BinaryTree:
    # Provide a root node to the constructor
    def __init__(self, root):
        self.root = root
    # Pretty prints the tree structure
    def prettyPrint(self):
        pass
    # Setter method for user
    def add(self, newNode):
        self.__traverseAdd(newNode, self.root)
    # Traverses tree and adds at the right location
    def __traverseAdd(self, newNode, curNode):
        if newNode.value < curNode.value:
            if curNode.leftChild == None:
                newNode.parent = curNode
                curNode.leftChild = newNode
                print "Added " + str(newNode.value) + " as left child of " + str(curNode.value)
            else:
                self.__traverseAdd(newNode, curNode.leftChild)
        elif newNode.value > curNode.value:
            if curNode.rightChild == None:
                newNode.parent = curNode
                curNode.rightChild = newNode
                print "Added " + str(newNode.value) + " as right child of " + str(curNode.value)
            else:
                self.__traverseAdd(newNode, curNode.rightChild)
        else:
            curNode.addDuplicate(newNode)
    # Getter method for user
    def find(self, value):
        return self.__traverseFind(value, self.root)
    # Traverses tree and finds node of given value
    def __traverseFind(self, value, curNode):
        if value < curNode.value:
            return self.__traverseFind(value, curNode.leftChild)
        elif value > curNode.value:
            return self.__traverseFind(value, curNode.rightChild)
        else:
            return curNode
    # Get tree as a sorted array
    def getSorted(self):
        pass
    # Get leftmost node
    def getLeftmost(self):
        node = self.root
        while node.leftChild != None or node.rightChild != None:
            if node.leftChild != None:
                node = node.leftChild
            else:
                node = node.rightChild
        return node
    # Get leftmost node
    def getRightmost(self):
        node = self.root
        while node.rightChild != None or node.leftChild != None:
            if node.rightChild != None:
                node = node.rightChild
            else:
                node = node.leftChild
        return node
    # Get max value node
    def getMax(self):
        node = self.root
        while node.rightChild != None:
            node = node.rightChild
        return node
    # Get min value node
    def getMin(self):
        node = self.root
        while node.leftChild != None:
            node = node.leftChild
        return node

# Create a some nodes
a = BinaryNode(1,'apple')
b = BinaryNode(6,'bank')
c = BinaryNode(3,'card')
d = BinaryNode(8,'dog')
e = BinaryNode(12,'elephant')
f = BinaryNode(2,'ferd')
g = BinaryNode(5,'gog')
h = BinaryNode(9,'help')

# Create a tree
tree = BinaryTree(g)
tree.add(a)
tree.add(b)
tree.add(c)
tree.add(d)
tree.add(e)
tree.add(h)
tree.add(f)

# TODO
tree.prettyPrint()
