"""Function take the str parameter being passed and return the first word with
greatest number of repeated letters:
>>> greatest_repeated_letters("Hello apple pie")
'Hello'
>>> greatest_repeated_letters("No words")
-1
"""

def greatest_repeated_letters(words):
    """return the first word with greatest number of repeated letters"""
    words = words.split(' ')
    hash_map = {}
    index = 0
    current_repeats = 0
    max_repeats = 0
    no_repeats = True

    for i in range(len(words)):
        for y in range(len(words[i])):
            if words[i][y] not in hash_map:
                hash_map[words[i][y]] = 1
            else:
                hash_map[words[i][y]]+= 1
                no_repeats = False
        for char in hash_map:
            if hash_map[char] > 2:
                current_repeats+= hash_map[char]//2

        if max_repeats < current_repeats:
            max_repeats = current_repeats 
            index = i
        hash_map = {}
    if no_repeats == True:
        return -1    
    return words[index]   






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! You did it!')