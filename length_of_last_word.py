"""Given a string s consists of some words separated by spaces, return the length 
of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only
>>> length_last_word("Hello World")
5
>>> length_last_word(" ")
0
>>> length_last_word("a ")
1
"""

def length_last_word(s):
    """Return length of last word"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! Sweat heart!')