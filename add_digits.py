"""Given a non-negative integer num, repeatedly add all its digits until the
result has only one digit:
>>> add_digits(38)
2
>>> add_digits(199)
1
>>> add_digits(58)
4
"""

def add_digits(num):
    """Return one digit after repeatedly add"""
    #Right answer is remainder of the division
    if num%9==0 and num!=0:
        return 9
    else:
        return num%9




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ALL TESTS PASS! AWESOME JOB Young Padawan! \n')