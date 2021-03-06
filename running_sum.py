"""Given an array nums. We define a running sum of an array as 
runningSum[i] = sum(nums[0]…nums[i]).
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]:
>>> running_sum([1,2,3,4])
[1, 3, 6, 10]
>>> running_sum([1,1,1,1,1])
[1, 2, 3, 4, 5]
>>> running_sum([3,1,2,10,1])
[3, 4, 6, 16, 17]
"""

def running_sum(nums):
    """Return the running sum of nums"""
    current_sum = 0
    result = []
    for num in nums:
        current_sum+= num 
        result.append(current_sum)
    return result 




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! My heart is go oooon \u2764\uFE0F')