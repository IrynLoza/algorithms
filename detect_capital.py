"""Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way:
>>> is_capital("USA")
True
>>> is_capital("leetcode")
True
>>> is_capital("FlaG")
False
"""

def is_capital(word):
    """Return True if capitals in word is right

    Check if all word upper case -> word.isupper()
    or lower case -> word.islower() and return True
    Check if only first char upper case-->  (word[0].isupper() and word[1:].islower()) 
    and return True
    Overwise return False"""

    return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('ALL TESTS PASS! KEEP MOVING!')