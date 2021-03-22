"""Given an array nums, return true if the array was originally sorted in 
non-decreasing order, then rotated some number of positions (including zero). 
Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length 
such that A[i] == B[(i+x) % A.length], where % is the modulo operation:
>>> is_sorted([3,4,5,1,2])
True
>>> is_sorted([1,1,1])
True
>>> is_sorted([2,1,3,4])
False
>>> is_sorted([2,1])
True
"""

def is_sorted(nums):
    """Return True if array sorted in rotated, overwise return False"""
    sorted_nums = sorted(nums)
        
    for i in range(len(nums)):
        """
        last el, 0, 1...: to the end AND from start to last el, 0, 1...
        [-1:] + [:-1]
        [2, 3, 4, 5, 1]
        [0:] + [:0]
        [3, 4, 5, 1, 2]
        [1:] + [:1]
        [4, 5, 1, 2, 3]
        [2:] + [:2]
        [5, 1, 2, 3, 4]
        [3:] + [:3]
        [1, 2, 3, 4, 5]
        """
        temp = nums[i-1:] + nums[:i-1]
        if temp == sorted_nums:
            return True
    return False




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! One more step to the stars! ✨')