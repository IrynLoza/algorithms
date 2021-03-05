"""Given the array nums, for each nums[i] find out how many numbers 
in the array are smaller than it. That is, for each nums[i] you have 
to count the number of valid j's such that j != i and nums[j] < nums[i]:
>>> smaller_numbers([8,1,2,2,3])
[4, 0, 1, 1, 3]
>>> smaller_numbers([6,5,4,8])
[2, 1, 0, 3]
>>> smaller_numbers([7,7,7,7])
[0, 0, 0, 0]
"""

def smaller_numbers(nums):
    """Return the answer in an array"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Only forward to the stars! ✨')