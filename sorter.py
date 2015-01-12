class Sorter():
    def mergeSort(self, x):
        n = len(x)
        if n == 1:
            return x
        else:
            a = self.mergeSort(x[0:int(n/2)])
            b = self.mergeSort(x[int(n/2):])
            return self.mergeSortedList(a, b)
        
    def mergeSortedList(self, a, b):
        c = []
        while len(a) or len(b):
            if len(a) == 0:
                return c + b
            if len(b) == 0:
                return c + a
            if a[0] < b[0]:
                c.append(a[0])
                a.pop(0)
            elif a[0] > b[0]:
                c.append(b[0])
                b.pop(0)
            elif a[0] == b[0]:
                c.append(a[0])
                c.append(b[0])
                a.pop(0)
                b.pop(0)
        return c
    
# usage
sorter = Sorter()

# merge sort
print sorter.mergeSort([1, 3, 5, 7, 14 , 3, 4, 6, 8])
