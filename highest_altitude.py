"""There is a biker going on a road trip. The road trip consists of n + 1 
points at different altitudes. The biker starts his trip on point 0 with 
altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net 
gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return 
the highest altitude of a point:
>>> highest_altitude([-5,1,5,0,-7])
1
>>> highest_altitude([-4,-3,-2,-1,4,3,2])
0
"""

def highest_altitude(gain):
    """Return highest altitude"""
    altitudes = [0]
        
    for num in gain:
        next_num = num + altitudes[-1]
        altitudes.append(next_num)
    
    result = altitudes[0]
    for num in altitudes:
        if num > result:
            result = num
    return result




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! Dance time!')