"""Given a string S, return the "reversed" string where all characters that are not a 
letter stay in the same place, and all letters reverse their positions:
>>> reverseOnlyLetters("ab-cd")
"dc-ba"
>>> reverseOnlyLetters("a-bC-dEf-ghIj")
"j-Ih-gfE-dCba"
"""

def reverseOnlyLetters(S):
    """Return reversed letters only"""
    #Use as stack, to take last letter 
    letters = []
    
    #Store letters to list
    for letter in S:
        if letter.isalpha():
            letters.append(letter)
            
    result = []
    for char in S:
        if char.isalpha():
            result.append(letters.pop())
        else:
            result.append(char)
    
    return "".join(result)
    



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ALL TESTS PASS! YOU DID IT AGAIN! FORCE WITH YOU!')