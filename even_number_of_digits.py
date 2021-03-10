"""Given an array nums of integers, return how many of them contain an 
even number of digits.
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits:

>>> find_even([12,345,2,6,7896])
2
>>> find_even([555,901,482,1771])
1
"""

def find_even(nums):
    """Return how many of them contain an even number of digits"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Born to be STAR! ✨')