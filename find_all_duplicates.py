"""Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements 
appear twice and others appear once.

Find all the elements that appear twice in this array:
>>> duplicates([4,3,2,7,8,2,3,1])
[3, 2]
>>> duplicates([1,3,2,1,8,1,3,1])
[3]
"""

def duplicates(nums):
    """Return all duplicates appear twice"""
    hash_map = {}
        
    for num in nums:
        if num not in hash_map:
            hash_map[num] = 1
        else:
            hash_map[num]+= 1
    result = []
    for key in hash_map:
        if hash_map[key] > 1 and hash_map[key] <=2:
            result.append(key)
    return result  




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! Go go go!')