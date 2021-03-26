"""Given an integer n, add a dot (".") as the thousands separator 
and return it in string format:
>>> separator(987)
'987'
>>> separator(1234)
'1.234'
>>> separator(123456789)
'123.456.789'
"""

def separator(n):
    """Return with separator"""
    #reverse n
    n = str(n)[::-1]
    
    result = ''
    for i in range(len(n)):
        if i%3 == 0 and i>0:
            result  = result + '.'+ n[i]
        else:
            result = result + n[i]
    return ''.join(result)[::-1]




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! Did it again! Oh baby, baby!')