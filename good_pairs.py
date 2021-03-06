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
    result = 0
    hash_map = {}
    
    for num in nums:
        if num not in hash_map:
            hash_map[num] = 1
        else:
            hash_map[num]+= 1       
        
    for key in hash_map:
        result+= (hash_map[key]*(hash_map[key]-1))/2
    
    return int(result)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! You are SUPERNOVA ✨')