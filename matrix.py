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
