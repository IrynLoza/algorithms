"""International Morse Code defines a standard encoding where each letter 
is mapped to a series of dots and dashes, as follows: "a" maps to ".-", 
"b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet 
is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
"--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-",
"-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of 
the Morse code of each letter. For example, "cab" can be written as 
"-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll 
call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have:
>>> unique_words(["gin", "zen", "gig", "msg"])
2
>>> unique_words(["help", "me", "please"])
3
"""

def unique_words(words):
    """Return the number of unique morse words"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! Nice job!') 