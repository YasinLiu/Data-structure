"""
    # * Quicksort: memory usage is O(log n) in the best case and O(n) in the worst case. 
        1. Begin by selecting the item at the list’s midpoint. This item is called the pivot.
    (Later, this chapter covers alternative ways to choose the pivot.)
        2. Partition items in the list so that all items less than the pivot are moved to the
    left of the pivot, and the rest are moved to its right. The final position of the pivot
    itself varies, depending on the actual items involved. For instance, the pivot ends
    up being rightmost in the list if it is the largest item and leftmost if it is the
    smallest. But wherever the pivot ends up, that is its final position in the fully
    sorted list.
        3. Divide and conquer. Reapply the process recursively to the sublists formed by
    splitting the list at the pivot. One sublist consists of all items to the left of the pivot
    (now the smaller ones), and the other sublist has all items to the right (now the
    larger ones).
        4. The process terminates each time it encounters a sublist with fewer than two
    items.
"""
import numpy as np


def partion(lyst, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle], lyst[right] = lyst[right], lyst[middle]

    # Set boundary point to first position
    boundary = left

    # Move items less than pivot to left
    for index in range(left, right):
        if lyst[index] < pivot:
            lyst[index], lyst[boundary] = lyst[boundary], lyst[index]
            boundary += 1

    # Exchange the pivot item and the boundary item
    lyst[boundary], lyst[right] = lyst[right], lyst[boundary]
    return boundary


def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocattion = partion(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocattion-1)
        quicksortHelper(lyst, pivotLocattion+1, right)


if __name__ == '__main__':
    lyst = np.random.randint(50, size=10)
    print(lyst)
    # b = partion(lyst, 0, len(lyst)-1)
    quicksortHelper(lyst, 0, len(lyst)-1)
    print(lyst)
