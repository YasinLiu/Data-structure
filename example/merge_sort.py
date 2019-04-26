import numpy as np

def mergeSort(lyst):
    """ The function called by users
    
    Arguments:
        lyst {list} -- list being sorted
        copyBuffer {list} -- temporary space needed during merge
    """
    copyBuffer = [None] * len(lyst)  # * 避免在递归调用中重复分配，节省内存开销
    mergeSortHelper(lyst, copyBuffer, 0, len(lyst)-1)


def mergeSortHelper(lyst, copyBuffer, low, high):
    """ A helper function that hides the extra parameters required by recursive calls.
    
    Arguments:
        lyst {list} -- list being sorted
        copyBuffer {list} -- temp space needed during merge
        low, high {int} -- bounds of sublist
        middle {int} -- middlepoint of sublist
    """
    if low < high:
        middle = (low + high) // 2
        mergeSortHelper(lyst, copyBuffer, low, middle)
        mergeSortHelper(lyst, copyBuffer, middle+1, high)
        merge(lyst, copyBuffer, low, middle, high)


def merge(lyst, copyBuffer, low, middle, high):
    # Initialize i1, and i2 to the first items in each sublist
    i1 = low
    i2 = middle + 1

    # Interleave items from the sublists into the copyBuffer in such a way
    # that is maintained
    for i in range(low, high+1):
        if i1 > middle:
            copyBuffer[i] = lyst[i2] # First sublist exhausted
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = lyst[i1] # Second sublist exhausted
            i1 += 1
        elif lyst[i1] > lyst[i2]:
            copyBuffer[i] = lyst[i2] # Item in second sublist
            i2 += 1
        else:
            copyBuffer[i] = lyst[i1] # Item in first sublist
            i1 += 1

    # Copy sorted items back to proper position in lyst
    for i in range(low, high+1):
        lyst[i] = copyBuffer[i]


if __name__ == '__main__':
    lyst = np.random.randint(100, size=20)
    print(lyst)
    mergeSort(lyst)
    print(lyst)