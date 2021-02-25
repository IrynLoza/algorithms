""" Calculet sum of two strings and oncatenate them using following rules:
>>> sum_concatenation('99', '99')
'1818'
>>> sum_concatenation('12', '7')
'19'
>>> sum_concatenation('11', '9')
'110'
"""

def sum_concatenation(a, b):
    """Return concatenated string"""

    result = ''
    main = []
    second = []

    if len(a) >= len(b):
        main = a
        second = b
    else:
        main = b
        second = a

    second_length = len(second)

    i = 0
    while second_length > 0:
        temp = int(main[len(main)-(1+i)]) + int(second[len(second)-(1+i)])
        result = f'{temp}{result}'
        second_length-= 1 
        i+= 1

    rest_nums = main[:(len(main)-len(second))]  
    result = f'{rest_nums}{result}'   

    return result





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\u2764\uFE0F ALL TESTS PASS! You are doing great!')
