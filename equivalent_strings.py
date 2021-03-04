"""Given two string arrays word1 and word2, return true if the two arrays 
represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in 
order forms the string:
>>> is_equal(["ab", "c"], ["a", "bc"])
True
>>> is_equal(["a", "cb"], ["ab", "c"])
False
>>> is_equal(["abc", "d", "defg"], ["abcddefg"])
True
>>> is_equal(["abc", "d", "defg"], ["abcddef"])
False
"""

def is_equal(word1, word2):
    """Return true if the two arrays represent the same string, 
    and false otherwise"""
    word1_str = ''
    word2_str = ''
    
    for char in word1:
        word1_str = f'{word1_str}{char}'
    
    for char in word2:
        word2_str = f'{word2_str}{char}'
    
    if len(word1_str) != len(word2_str):
        return False
        
    index = 0 
    for i in range(len(word2)):
        for y in range(len(word2[i])):
            if word2[i][y] != word1_str[index]:
                return False
            index+= 1
            
    return True 




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! Force with you! \u2764\uFE0F')