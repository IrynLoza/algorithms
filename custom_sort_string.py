"""S and T are strings composed of lowercase letters. In S, no letter 
occurs more than once.

S was sorted in some custom order previously. We want to permute the 
characters of T so that they match the order that S was sorted. More 
specifically, if x occurs before y in S, then x should occur before y 
in the returned string:
>>> custom_sort("cba", "abcd")
'cbad'
"""

def custom_sort(S, T):
    """Return any permutation of T (as a string) that satisfies this property"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Go on Girl! ✨')