"""Given an array of integers arr, write a function absSort(arr), that sorts 
the array according to the absolute values of the numbers in arr. If two 
numbers have the same absolute value, sort them according to sign, where the 
negative numbers come before the positive numbers:
>>> abs_sort([2, -7, -2, -2, 0])
[0, -2, -2, 2, -7]
>>> abs_sort([-2,1])
[1, -2]
>>> abs_sort([-2,3,5,-1,4])
[-1, -2, 3, 4, 5]
"""

def abs_sort(arr):
    """Return sorted array in absolute order"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! You did it!')
