import itertools
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
    str_list1 = []
    for key, group in itertools.groupby(name):
        str_list1.append((key, len(list(group))))
    #print(str_list1)
    #[('a', 1), ('l', 1), ('e', 1), ('x', 1)]
    str_list2 = []
    for key, group in itertools.groupby(typed):
        str_list2.append((key, len(list(group))))
    #print(str_list2)
    #[('a', 2), ('l', 1), ('e', 2), ('x', 1)]
    
    if len(str_list1) != len(str_list2):
        return False
    
    #all() method returns True when all elements in the given iterable are true
    #zip() function takes iterables (can be zero or more), aggregates them in a tuple, and return it
    return all(key1 == key2 and value1 <= value2
                for (key1,value1), (key2,value2) in zip(str_list1, str_list2))




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Monday is time for the new wins! ✨')