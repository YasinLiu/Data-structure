"""
    Bubble Sorted
"""
import numpy as np

def bubble_sort(lyst):
    n = len(lyst)
    while n > 1:
        swapped = True
        i = 1
        while i < n:
            if lyst[i] < lyst[i-1]:
                lyst[i], lyst[i-1] = lyst[i-1], lyst[i]
                swapped = True
            i += 1
        if not swapped: return
        n -= 1

    
if __name__ == '__main__':
    list1 = np.random.randint(100, size=20)
    print(list1)
    bubble_sort(list1)
    print(list1)