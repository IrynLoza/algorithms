"""Implement quick sort
>>> quickSort([3,5,6,1,2,8])
[1, 2, 3, 5, 6, 8]
>>> quickSort([1,2,3])
[1, 2, 3]
>>> quickSort([])
[]
>>> quickSort([3,5,6,1,2,3,2,8])
[1, 2, 2, 3, 3, 5, 6, 8]
"""

def quickSort(arr):
    pass



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('You sort it!')