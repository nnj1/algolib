#!/bin/pyhton3
"""
Simple script that returns a list of size n filled with random values within
a provided limit
"""
import random

def createRandArray(n, lim):
    temp = []
    for i in range(n):
        temp.append(random.randrange(lim))
    return temp


# Usage
if __name__ == '__main__':
    print(createRandArray(10, 100))
