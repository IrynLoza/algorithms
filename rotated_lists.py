"""You are given list of numbers, obtained by rotating a sorted list an 
unknown number of times. Write a function to determine the minimum number 
of times the original sorted list was rotated to obtain the given list. 
Your function should have the worst-case complexity of O(log N), where N is 
the length of the list. You can assume that all the numbers in the list are 
unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted 
list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and 
adding it before the first element. E.g. rotating the list [3, 2, 4, 1] 
produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the 
increasing order e.g. [1, 3, 5, 7]:
>>> count_rotations([19, 25, 29, 3, 5, 6, 7, 9, 11, 14])
3
>>> count_rotations([3, 5, 7, 9, 10, 0, 1, 2])
5
>>> count_rotations([1, 2, 3, 4, 5, 6, 7, 8, 9])
0
>>> count_rotations([2,1])
1
>>> count_rotations([])
0
"""

def count_rotations(nums):
    """Return number of rotations"""
    #Brute force
    """position = 0                
    
    while position < len(nums):                     
        if position > 0 and nums[position] < nums[position-1]:   
            return position
        position += 1
    
    return 0"""

    #Binary search
    lo = 0
    hi = len(nums)-1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = nums[mid]
        
        
        if mid > 0 and mid_number < nums[mid-1]:
            # The middle position is the answer
            return mid
        
        elif mid_number < nums[hi]:
            # Answer lies in the left half
            hi = mid - 1  
        
        else:
            # Answer lies in the right half
            lo = mid + 1
    
    return 0




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Only better forward! ✨')