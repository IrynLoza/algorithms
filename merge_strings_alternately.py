"""You are given two strings word1 and word2. Merge the strings by adding 
letters in alternating order, starting with word1. If a string is longer 
than the other, append the additional letters onto the end of the merged string.

Return the merged string:
>>> merge_alternately("abc", "pqr")
'apbqcr'
>>> merge_alternately("ab", "pqrs")
'apbqrs'
>>> merge_alternately("abcd", "pq")
'apbqcd'
"""

def merge_alternately(word1, word2):
    """Return the merged string"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Go IRYN! ✨')
