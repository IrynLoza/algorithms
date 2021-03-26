"""You are given a string text of words that are placed among some number of 
spaces. Each word consists of one or more lowercase English letters and are 
separated by at least one space. It's guaranteed that text contains at least 
one word.

Rearrange the spaces so that there is an equal number of spaces between every 
pair of adjacent words and that number is maximized. If you cannot redistribute 
all the spaces equally, place the extra spaces at the end, meaning the returned 
string should be the same length as text:
>>> rearranging_spaces("  this   is  a sentence ")
'this   is   a   sentence'
>>> rearranging_spaces(" practice   makes   perfect")
'practice   makes   perfect '
>>> rearranging_spaces("hello   world")
'hello   world'
"""


def rearranging_spaces(text):
    """Return the string after rearranging the spaces"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! Did it again! Oh baby, baby!')