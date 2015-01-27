from randArray import createRandArray

"""
The insertion sort algorithm works on the assumption that the sub-array to the
left of the key is already sorted.

It iteratively inserts the key into the proper position in the sorted sub-array
and increments the key value on each iteration
"""
def insertionSort(_list):
    # initializing j to the second item of the list
    j = 1
    while j < len(_list):
        # initializing the key
        key = _list[j]
        # setting the loop invariant for the inner loop which compares and
        # increments the position of each item of the sub array
        i = j - 1
        # moving each item of the sub array until the proper position of the
        # key is found
        while i >=0 and _list[i] > key:
            _list[i+1] = _list[i]
            i = i - 1
        # inserting the key into it's proper position
        _list[i + 1] = key
        j = j + 1
    return _list

if __name__ == '__main__':
    # Using the random array function to create a random array to test
    # insertion sort
    print(insertionSort(createRandArray(10,100)))


