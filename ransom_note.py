"""Given an arbitrary ransom note string and another string containing letters from all the 
magazines, write a function that will return true if the ransom note can be constructed from 
the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note:
>>> ransom_note('a','b')
False
>>> ransom_note('aa','ab')
False
>>> ransom_note('aa','aab')
True
"""

def ransom_note(ransomNote, magazine):
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('ALL TESTS PASS! I am proud of you!')