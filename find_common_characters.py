"""Given an array A of strings made only from lowercase letters, return a 
list of all characters that show up in all strings within the list (including 
duplicates).  For example, if a character occurs 3 times in all strings but 
not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order:
>>> commonChars(["bella","label","roller"])
['e', 'l', 'l'])
>>> commonChars(["cool","lock","cook"])
['c', 'o'])
"""

def commonChars(A):
    """Return common chars"""




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! Do not give up')    