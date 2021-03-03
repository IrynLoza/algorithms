"""You are given two strings word1 and word2. Merge the strings by adding 
letters in alternating order, starting with word1. If a string is longer 
than the other, append the additional letters onto the end of the merged string.

Return the merged string:
>>> merge_alternately("abc", "pqr")
'apbqcr'
>>> merge_alternately("ab", "pqrs")
'apbqrs'
>>> merge_alternately("abcd", "pq")
'apbqcd'
"""

def merge_alternately(word1, word2):
    """Return the merged string"""
    length = 0
    main = ''
    
    if len(word1) >= len(word2):
        length = len(word2)
        main = word1
    else:
        length = len(word1)
        main = word2
        
    result = ''    
    for i in range(length):
        result = f'{result}{word1[i]}{word2[i]}'
    
    if len(main) > length:
        rest = main[length:]
        result = f'{result}{rest}'
        
    return result




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Go IRYN! ✨')
