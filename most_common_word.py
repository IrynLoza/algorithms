"""Given a paragraph and a list of banned words, return the most frequent word that is not 
in the list of banned words.  It is guaranteed there is at least one word that isn't banned, 
and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in 
the paragraph are not case sensitive.  The answer is in lowercase.
>>> most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
'ball'
>>> most_common_word("Bob. hIt, baLl", ["bob", "hit"])
'ball'
>>> most_common_word("a, a, a, a, b,b,b,c, c", ["a"])
'b'
"""

def most_common_word(paragraph, banned):
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ALL TEST PASS! KEEP MOVING!')