"""Given an integer n, return any array containing n unique integers such 
that they add up to 0.
>>> sum_zero(5)
[-2, -1, 0, 1, 2]
>>> sum_zero(10)
[-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
>>> sum_zero(3)
[-1, 0, 1]
>>> sum_zero(1)
[0]
"""

def sum_zero(n):
    """Return array with sum zero"""
    if n == 1:
        return [0]
    
    result = []
    #Take the first num 
    first = -(n // 2)
    
    for i in range(n):
        #Increase by 1 if 0 and not %
        if first == 0 and not n%2:
            first += 1
        #Add to result    
        result.append(first)
        #increase
        first += 1
    return result
    




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Nailed it! ✨')