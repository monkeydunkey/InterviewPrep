'''
Randomly shuffle an array and return the result
'''
import random
import sys

def shuffle(arr):
    for i, a in enumerate(arr):
        r = random.randint(0, i)
        arr[i], arr[r] = arr[r], arr[i]
    return arr

arr = sys.argv[1:]
print shuffle(arr)

