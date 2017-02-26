class Matrix:
    def __init__(self, mat, c = 0):
        # Get r and c based on given mat
        if isinstance(mat, list):
            self.mat = mat
            self.r = len(mat)
            self.c = len(mat[0])
        # Construct a zero initialized mat based on r and c
        else:
            self.r = mat
            self.c = c
            self.mat = []
            i = 0
            k = []
            while i < c:
                k.append(0)
                i += 1
            i = 0
            while i < mat:
                self.mat.append(k)
                i += 1
    def prettyPrint(self):
        for row in self.mat:
            print row
    def add(self, b):
        summat= []
        i = 0
        for row in b.mat:
            j = 0
            summat.append([])
            for element in row:
                summat[i].append(self.mat[i][j] + element)
                j += 1
            i += 1
        return Matrix(summat)
    def scalarMultiply(self, k):
        i = 0
        for row in self.mat:
            j = 0
            for element in row:
                self.mat[i][j] = k * element
                j += 1
            i += 1
    def getElement(self, row, column):
        return self.mat[row - 1][column - 1]
    def getRow(self, row):
        return self.mat[row - 1]
    def getColumn(self, cn):
        column = []
        for row in self.mat:
            column.append(row[cn - 1])
        return column
    def setElement(self, row, column, v):
        self.mat[row - 1][column - 1] = v
    def dotProduct(self, a, b):
        sum = 0
        for i, val in enumerate(a):
            sum += (val + b[i])
        return sum
    def multiply(self, b):
        if self.c == b.r:
            pmat = []
            for i, row in enumerate(self.mat, start=1):
                pmat.append([])
                for j, item in enumerate(row, start=1):
                    pmat[i - 1].append(self.dotProduct(self.getRow(i), b.getColumn(j)))
            return Matrix(pmat)
# usage
matrix1 = Matrix([[1,1,1],[0,0,0],[2,3,4]])
print "Initialized Matrix:"
matrix1.prettyPrint()

print "Scalar Multiplication by 2"
matrix1.scalarMultiply(2)
matrix1.prettyPrint()

matrix2 = Matrix([[1,1,1],[1,0,1],[1,1,1]])
print "Initialized 2nd Matrix:"
matrix2.prettyPrint()

matrix3 = matrix1.add(matrix2)
print "Sum:"
matrix3.prettyPrint()

print "Element in 2rd row and 3rd column: " + str(matrix3.getElement(2,3))
print '3rd Row: ' + str(matrix3.getRow(3))
print '3rd Column: ' + str(matrix3.getColumn(3))

print "Product:"
print str(matrix3.multiply(matrix2).prettyPrint())
