"""
    Binary seach
    Exercise 3.3 
    1. Suppose that a list contains the values 20, 44, 48, 55, 62, 66, 74, 88, 93, 99 at index
positions 0 through 9. Trace the values of the variables left , right , and midpoint in
a binary search of this list for the target value 90. Repeat for the target value 44.
"""

def binary_search(target, sorted_list):
    left = 0
    right = len(sorted_list) - 1
    print('{:>10}{:>10}{:>10}'.format('left', 'mid', 'right'))
    while left <= right:
        mid = (left + right) // 2
        print('{:>10d}{:>10d}{:>10d}'.format(left, mid, right))
        if target == sorted_list[mid]:
            return mid
        elif target < sorted_list[mid]:
            right = mid -1
        else:
            left = mid + 1
    print('no result')
    return -1

if __name__ == '__main__':
    list1 = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]
    mid = binary_search(44, list1)   
    print('position:{:>10d}; value:{:>10d}'.format(mid, list1[mid]))