"""Find square root of a large number in O(logn) time:
>>> square_root(10)
3
>>> square_root(1000000)
1000
>>> square_root(262)
16
>>> square_root(1)
1
"""

def square_root(num):
    """Return square root of given number"""
    lo = 1
    hi = num

    while lo <= hi:
        mid = (lo+hi) // 2
        if num // mid == mid:
            return mid
        elif num // mid < mid:
            #left side
            hi = mid - 1
        else:
            #rigth side
            lo = mid + 1

            


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Go IRYN! ✨')