"""Given two binary strings a and b, return their sum as a binary string:
>>> add_binary('11', '1')
'100'
>>> add_binary('1010', '1011')
'10101'
"""

def add_binary(a, b):
    """Return sum in binary"""
    """11 -> 3
            1 -> 1
            ==>>> 4 == 100 binary
              
    """
    def to_decimal(num):
        base = 1
        devimal_value = 0
        
        for i in range(len(num)-1, -1, -1):
            if num[i] == '1':
                devimal_value+= base
            base = base*2
        return  devimal_value
    
    decimal_ab = to_decimal(a) + to_decimal(b)
    
    def to_binary(decimal_number):
        if decimal_number == 0:
            return 0
        else:
            return (decimal_number % 2 + 10 * to_binary(int(decimal_number // 2)))
        
    return str(to_binary(decimal_ab))






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Only better forward! ✨')