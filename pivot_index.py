"""Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the 
left of the index is equal to the sum of all the numbers strictly to the index's 
right.

If the index is on the left edge of the array, then the left sum is 0 because 
there are no elements to the left. This also applies to the right edge of the 
array:
>>> pivot_index([1,7,3,6,5,6])
3
>>> pivot_index([1,2,3])
-1
>>> pivot_index([2,1,-1])
0
"""

def pivot_index(nums):
    """Return the leftmost pivot index. If no such index exists, return -1"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! Dance like a star!!!')