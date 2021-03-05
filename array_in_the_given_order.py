"""Given two arrays of integers nums and index. Your task is to create 
target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the 
value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid:
>>> target_array([0,1,2,3,4], [0,1,2,2,1])
[0, 4, 1, 3, 2]
>>> target_array([1,2,3,4,0], [0,1,2,3,0])
[0, 1, 2, 3, 4]
>>> target_array([1], [0])
[1]
"""

def target_array(nums, index):
    """Return the target array"""
    result = []
    for i in range(len(index)):
        result.insert(index[i], nums[i])
    
    return result




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! All stars are yours! ✨')