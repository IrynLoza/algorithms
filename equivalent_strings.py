"""Given two string arrays word1 and word2, return true if the two arrays 
represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in 
order forms the string:
>>> is_equal(["ab", "c"], ["a", "bc"])
True
>>> is_equal(["a", "cb"], ["ab", "c"])
False
>>> is_equal("abc", "d", "defg"], ["abcddefg"])
True
>>> is_equal(["abc", "d", "defg"], ["abcddef"])
False
"""

def is_equal(word1, word2):
    """Return true if the two arrays represent the same string, 
    and false otherwise"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! Force with you! \u2764\uFE0F')