import random

class Knuth:
    def __init__(self):
        pass
    def shuffle(self, a):
        i = 0
        while i < len(a):
            r = random.randint(0,i)
            temp = a[i]
            a[i] = a[r]
            a[r] = temp
            i += 1
        return a

# demo
knuth = Knuth()
print knuth.shuffle([1,2,3,4,5,6,7,8,9,10])
