"""You are given a string s, return the number of segments in the string. 

A segment is defined to be a contiguous sequence of non-space characters:
>>> count_segments("Hello, my name is John")
5
>>> count_segments("")
0
>>> count_segments("love live! mu'sic forever")
4
"""

def count_segments(s):
    """Return number of segments"""
    s = s.strip().split()
    return len(s)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! You are shine! ✨')

