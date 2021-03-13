"""Convert binary string to decimal number
1     0    0    1    0    1
2*5  2*4  2*3  2*2  2*1  2*0 
32    16   8   4    2    1
32     0    0   4    0    1
===> 37
>>> binary_to_decimal("100101") 
37
>>> binary_to_decimal("10011100")
156
"""

def binary_to_decimal(str):
    """Return decimal number"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Winner! ✨')
