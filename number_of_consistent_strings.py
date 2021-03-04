"""You are given a string allowed consisting of distinct characters and an 
array of strings words. A string is consistent if all characters in the 
string appear in the string allowed.

Return the number of consistent strings in the array words:
>>> count_consistent_strings("ab", ["ad","bd","aaab","baa","badab"])
2
>>> count_consistent_strings("abc", ["a","b","c","ab","ac","bc","abc"])
7
>>> count_consistent_strings("cad", ["cc","acd","b","ba","bac","bad","ac","d"])
4
"""

def count_consistent_strings(allowed, words):
    """Return the number of consistent strings in the array words"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! One more step! ✨')