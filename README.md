[algolib]() - A Collection of Reuseable Algorithms
=======

#Installation
Just clone and use.
```bash
$ git clone https://github.com/nnj1/algolib.git
$ python
>>> import algolib
```

#Differential Equations
##Euler Approximation
```python
# Euler.approx(y' = f(t,y), x0, y0, stepsize, maxiterations)
euler = Euler()
data = euler.approx(lambda t,y : 2*(y**3) + t**2, 0, -0.5, 0.1, 20)
```
```data``` is a list of lists that are respective to each iteration (```[i,t,y,dy/dt]```)

##Runge-Kutta Approximation
```python
# RK4.approx(y' = f(t,y), x0, y0, stepsize, maxiterations)
kutta = RK4()
data = kutta.approx(lambda t,y : y/2 + t, 0, -0.5, 0.1, 100)
```
```data``` is a list of lists that are respective to each iteration (```[i,t,y,dy/dt]```)

#Hashing
```python
# Create hashing lambda function
algo = lambda key: int((ord(key[1]) + ord(key[0])) * math.sqrt(ord(key[0]) * ord(key[1])))

# Create hash table based on lambda function
table = HashTable(algo)

# Add some stuff to the table 
# HashTable.push(key, content)
table.push('Name', 'Swag')
table.push('Age', 17)

# Look up some stuff
print table.lookUp('Name')
print table.lookUp('Age')
```

#Sorting
```python
# usage
sorter = Sorter()

# the sorts
print sorter.mergeSort([1, 3, 5, 7, 14 , 3, 4, 6, 8])
print sorter.quickSort([1, 3, 5, 7, 14 , 3, 4, 6, 8])
print sorter.insertionSort([1, 3, 5, 7, 14 , 3, 4, 6, 8])
print sorter.selectionSort([1, 3, 5, 7, 14 , 3, 4, 6, 8])
# pass in initial gap size as additional arg
print sorter.shellSort([1, 3, 5, 7, 14 , 3, 4, 6, 8], 3)
```

#Matrix Functions
```python
# usage and initialization
matrix1 = Matrix([[1,1,1],[0,0,0],[2,3,4]])
matrix2 = Matrix([[1,1,1],[1,0,1],[1,1,1]])

# pretty printing
matrix1.prettyPrint()

# scalar multiplication
matrix1.scalarMultiply(2)

# addition
matrix3 = matrix1.add(matrix2)

# multiplication
matrix4 = matrix3.multiply(matrix2)

# dot product (only works for column and row vectors)
TODO

# getters and setters
matrix3.getElement(2,3)
matrix3.getRow(3)
matrix3.getColumn(3)
matrix3.setElement(2,3,thing)

```

