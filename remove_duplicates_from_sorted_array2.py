"""Given a sorted array nums, remove the duplicates in-place such that duplicates 
appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying 
the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer, but your answer is an array?

Note that the input array is passed in by reference, which means a modification 
to the input array will be known to the caller:
>>> remove_duplicates([1,1,1,2,2,3])
5
>>> remove_duplicates([0,0,1,1,1,1,2,3,3])
7
"""

def remove_duplicates(nums):
    """Remove third duplicate and return length of updated array"""
    if len(nums)<3:
        return len(nums)
    
    i=2
    while i<len(nums):
        if nums[i]==nums[i-2]:
            nums.pop(i)
        else:
            i+=1
    return len(nums)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! Did it again! Oh baby, baby!')