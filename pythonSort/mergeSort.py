from randArray import createRandArray
"""
The merge sort algorithm is a divide and conquer algorithm which divides the
given array into smaller arrays until the base case is reached, after which
the merge operation is performed.

The base case of this sorting algorithm is the condition that an array of
length 1 is already sorted and hence can be returned as it is.
"""
def mergeSort(_list):
    # return if given list is of length 1
    # This is the base case
    if len(_list) <= 1:
        return _list
    else :
        # calculate the mid point
        mid = len(_list) // 2

        # Split the given array into 2
        left = _list[:mid]
        right = _list[mid:]

        # resursively call mergesort to get left and right half of the given
        # array
        left = mergeSort(left)
        right = mergeSort(right)

        # Call merge on the left and right arrays
        return list(merge(left, right))

def merge(left, right):
    # initialize the result list
    result = []

    # initializing the indices
    leftIndex, rightIndex = 0, 0

    # the indices are used as loop invariants and the loop runs until the end
    # of one of the arrays is reached
    while leftIndex < len(left) and rightIndex < len(right):
        # if we reverse this comparison the direction of the sort is reversed
        if left[leftIndex] <= right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex = leftIndex + 1
        else:
            result.append(right[rightIndex])
            rightIndex = rightIndex + 1

    # at the end of the loop if either of the two arrays is left, it implies
    # that all the elements of the array that is left is larger than the
    # elements currently present in the result array.
    if left:
        result.extend(left[leftIndex:])
    if right:
        result.extend(right[rightIndex:])

    return result

# usage
if __name__ == '__main__':
    x = createRandArray(10,1000)
    print(x)
    print(mergeSort(x))
