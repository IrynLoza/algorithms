"""Given a string text, you want to use the characters of text to form as 
many instances of the word "balloon" as possible.

You can use each character in text at most once:
>>> balloon_numbers("nlaebolko")
1
>>> balloon_numbers("leetcode")
0
>>> balloon_numbers("loonbalxballpoon")
2
"""

def balloon_numbers(text):
    """Return the maximum number of instances that can be formed"""
    hash_map = { 'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

    for char in text:
        if char in hash_map:
            hash_map[char]+= 1
    hash_map['l']//2
    hash_map['o']//2  

    return min(hash_map.values())     




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Move forward! ✨')