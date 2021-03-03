"""You are given an integer array nums. The unique elements of an array are 
the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums:
>>> unique_sum([1,2,3,2])
4
>>> unique_sum([1,1,1,1])
0
>>> unique_sum([1,2,3,4,5])
15
>>> unique_sum([1,15,3,3,1,27,8,9,8])
51
"""

def unique_sum(nums):
    """Return the sum of all the unique elements of nums"""
    result = 0
    hash_map = {}
    
    for num in nums:
        if num not in hash_map:
            hash_map[num] = 1
        else:
            hash_map[num]+= 1 
    
    for num in hash_map:
        if hash_map[num] == 1:
            result+= num
    
    return result




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! You are a hash maps star!✨')