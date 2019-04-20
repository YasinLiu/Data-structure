"""
    Insertion sort
"""
import numpy as np


def Insertion_sort(lyst):
    i = 1  # 从第二个数开始往前插
    while i < len(lyst):
        item_to_insert = lyst[i]
        j = i - 1
        # 将第i个数插入到前i-1个已经排序好的数列中的正确位置
        while j >= 0:
            if item_to_insert < lyst[j]:
                lyst[j+1] = lyst [j]
                j -= 1
            else:
                break
        lyst[j+1] =item_to_insert
        i += 1


if __name__ == '__main__':
    lyst = np.random.randint(100, size=50)
    print(lyst)
    Insertion_sort(lyst)
    print(lyst)