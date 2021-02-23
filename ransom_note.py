"""Given an arbitrary ransom note string and another string containing letters from all the 
magazines, write a function that will return true if the ransom note can be constructed from 
the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note:
>>> is_ransom_note('a','b')
False
>>> is_ransom_note('aa','ab')
False
>>> is_ransom_note('aa','aab')
True
"""

def is_ransom_note(ransomNote, magazine):
    """Return True if can collect ransomNote from magazine"""

    for char in ransomNote:
        if char not in magazine:
            return False
        else:
            magazine = magazine.replace(char, '', 1)
    return True




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('ALL TESTS PASS! I am proud of you!')