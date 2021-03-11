"""Given words first and second, consider occurrences in some text of the 
form "first second third", where second comes immediately after first, and 
third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer:
>>> find_ocurrences("alice is a good girl she is a good student", "a", "good")
["girl", "student"]
>>> find_ocurrences("we will we will rock you", "we", "will")
["we","rock"]
>>> find_ocurrences("i love dogs because i love", "i", "love")
["dogs"]
"""

def find_ocurrences(text, first, second):
    """Return third occurrence"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Keep going! ✨')