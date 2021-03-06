"""Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.
>>> good_pair([1,2,3,1,1,3])
4
>>> good_pair([1,1,1,1])
6
>>> good_pair([1,2,3])
0
"""

def good_pair(nums):
    """Return the number of good pairs"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! You are SUPERNOVA ✨')