import math

class HashTable:
    # Constr
    def __init__(self, algo):
        self.algo = algo
        self.data = []
    # Turns a key into an index
    def __hashFunction(self, key):
         # shitty hash
        index = self.algo(key)
        if index > len(self.data):
            adds = index - len(self.data) + 1
            i = 0
            while i <= adds:
                self.data.append(None)
                i += 1
        return index
    # Pushes data into the table
    def push(self, key, value):
        index = self.__hashFunction(key)
        self.data[index] = value
    def lookUp(self, key):
        return self.data[self.__hashFunction(key)]

# Create hashing lambda function
algo = lambda key: int((ord(key[1]) + ord(key[0])) * math.sqrt(ord(key[0]) * ord(key[1])))
# Create hash table based on lambda function
table = HashTable(algo)
# Add some stuff to the table
table.push('Name', 'Swag')
table.push('Age', 17)

# Look up some stuff
print table.lookUp('Name')
print table.lookUp('Age')

