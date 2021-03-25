"""Given an array of integers nums sorted in ascending order, find the 
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1]:
>>> search_range([5,7,7,8,8,10], 8)
[3, 4]
>>> search_range([5,7,7,8,8,10], 6)
[-1, -1]
>>> search_range([], 0)
[-1, -1]
"""

def search_range(nums, target):
    """Return first and last position of given element or -1"""
    result = []
    for i in range(len(nums)):
        if nums[i] == target:
            result.append(i)  
    
    if len(result) == 0:
        return [-1, -1]
    else:
        return [result[0], result[-1]]




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! Did it again! Oh baby, baby!')