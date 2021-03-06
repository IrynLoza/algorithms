"""You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. Each character in stones is a type 
of stone you have. You want to know how many of the stones you have are also 
jewels.

Letters are case sensitive, so "a" is considered a different type of stone from 
"A".
>>> jewels_in_stones("aA", "aAAbbbb")
3
>>> jewels_in_stones("z", "ZZ")
0
"""

def jewels_in_stones(jewels, stones):
    """Return num of jewels in stones"""
    result = 0
    for i in range(len(stones)):
        if stones[i] in jewels:
            result+= 1
    return result




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
         print('\n \u2764\uFE0F ALL TESTS PASS! One more win! \u2764\uFE0F')