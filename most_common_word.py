import string
"""Given a paragraph and a list of banned words, return the most frequent word that is not 
in the list of banned words.  It is guaranteed there is at least one word that isn't banned, 
and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in 
the paragraph are not case sensitive.  The answer is in lowercase:
>>> most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
'ball'
>>> most_common_word("Bob. hIt, baLl", ["bob", "hit"])
'ball'
>>> most_common_word("a, a, a, a, b,b,b,c, c", ["a"])
'b'
"""

def most_common_word(paragraph, banned):
    """Return the most frequent word that is not in the list of banned words"""
    
    paragraph = paragraph.lower()
        
    #Remove punctuation
    exclude = set(string.punctuation)
    new_paragraph = ''
    devicer = ' '
    for char in paragraph:
        if char not in exclude:
            new_paragraph = f'{new_paragraph}{char}'
        else:
            new_paragraph = f'{new_paragraph}{devicer}'
        
    new_paragraph = new_paragraph.split(' ')

    words = {}
    for word in new_paragraph:
        if word not in banned and word != '':
            if word not in words:
                    words[word] = 1
            else:
                words[word]+= 1
    value = max(words.values())
    
    for word in words:
        if words[word] == value:
            return word




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ALL TEST PASS! KEEP MOVING!')