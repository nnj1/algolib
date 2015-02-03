import random

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

    def quickSort(self, x, lo = 0, hi = None):
        if hi == None:
            hi = len(x) - 1
        if lo < hi:
            p = self.partition(x, lo, hi)
            self.quickSort(x, lo, p - 1)
            self.quickSort(x, p + 1, hi)
        return x
    def partition(self, x, lo, hi):
        pi = self.choosePivot(x, lo, hi)
        pv = x[pi]
        temp = x[pi]
        x[pi] = x[hi]
        x[hi] = temp
        si = lo
        i = lo
        while i < hi:
            if x[i] < pv:
                temp = x[i]
                x[i] = x[si]
                x[si] = temp
                si += 1
            i += 1
        temp = x[si]
        x[si] = x[hi]
        x[hi] = temp
        return si
    def choosePivot(self, x, lo, hi):
        return random.randint(lo, hi)
    
# usage
sorter = Sorter()

# merge sort
print sorter.mergeSort([1, 3, 5, 7, 14 , 3, 4, 6, 8])
print sorter.quickSort([1, 3, 5, 7, 14 , 3, 4, 6, 8])
