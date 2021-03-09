"""In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every 
other number in the array.
>>> twice_largest([3, 6, 1, 0])
1
>>> twice_largest([1, 2, 3, 4])
-1
>>> twice_largest([0, 0, 0, 1])
3
"""

def twice_largest(nums):
    """Return the index of the largest element, otherwise return -1"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Brilliant job! ✨')