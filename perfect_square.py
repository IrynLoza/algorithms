"""Given a positive integer num, write a function which returns True 
if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt:
>>> is_perfect(16)
True
>>> is_perfect(14)
False
"""

def is_perfect(num):
    """Return True if square root is perfect or False if not"""
    lo = 1
    hi = num
    
    while lo <= hi:
        mid = (lo+hi) // 2
        if num / mid == mid:
            return True
        elif num / mid < mid:
            hi = mid -1
        else:
            lo = mid + 1
    return False




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! Higher every time!')