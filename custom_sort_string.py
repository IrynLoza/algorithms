"""S and T are strings composed of lowercase letters. In S, no letter 
occurs more than once.

S was sorted in some custom order previously. We want to permute the 
characters of T so that they match the order that S was sorted. More 
specifically, if x occurs before y in S, then x should occur before y 
in the returned string:
>>> custom_sort("cba", "abcd")
'cbad'
>>> custom_sort("kqep", "pekeq")
'kqeep'
"""

def custom_sort(S, T):
    """Return any permutation of T (as a string) that satisfies this property"""
    T_list = list(T)
    index = 0
    for char in S:
        for i in range(index, len(T_list)):
            if T_list[i] == char:
                T_list[i], T_list[index] = T_list[index], T_list[i]
                index += 1   

    return ''.join(T_list)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Go on Girl! ✨')