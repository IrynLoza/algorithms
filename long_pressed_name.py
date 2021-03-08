"""Your friend is typing his name into a keyboard. Sometimes, when typing a 
character c, the key might get long pressed, and the character will be typed 
1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible 
that it was your friends name, with some characters (possibly none) being long 
pressed:
>>> is_name("alex", "aaleex")
True
>>> is_name("saeed", "ssaaedd")
False
>>> is_name("leelee", "lleeelee")
True
>>> is_name("laiden", "laiden")
True
"""

def is_name(name, typed):
    """Return True if yes, overwise return false"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Monday is time for the new wins! ✨')