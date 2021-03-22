"""Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. If target 
exists, then return its index. Otherwise, return -1:
>>> binary_search([-1,0,3,5,9,12], 9)
4
>>> binary_search([-1,0,3,5,9,12], 2)
-1
"""

def binary_search(nums, target):
    """Return index of target element in array or -1 if not exist"""
    lo = 0
    hi = len(nums)-1
    
    while lo <= hi:
        mid = (lo+hi) // 2
        center = nums[mid]
        
        if center == target:
            return mid
        elif center < target:
            #target in a rigth side
            lo = mid+1
        else:
            #target in a left side
            hi = mid-1
    return -1




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! One more step to the job!')