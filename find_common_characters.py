"""Given an array A of strings made only from lowercase letters, return a 
list of all characters that show up in all strings within the list (including 
duplicates).  For example, if a character occurs 3 times in all strings but 
not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order:
>>> commonChars(["bella","label","roller"])
['e', 'l', 'l']
>>> commonChars(["cool","lock","cook"])
['c', 'o']
"""

def commonChars(A):
    """Return common chars"""
    hash_map = {}
        
    #Store letters from the first word
    for i in range(len(A[0])):
        if A[0][i] not in hash_map:
            hash_map[A[0][i]] = 1
        else:
            hash_map[A[0][i]]+= 1
    
    #Iterate througth each key in hash and rest of words
    for key in hash_map:
        for i in range(1,len(A)):
            #If char from first word in the word
            if key in A[i]:
                #Find min between count char from first word and next word
                hash_map[key] = min(hash_map[key], A[i].count(key))
            else:
                #Overwise nullify value and break
                hash_map[key] = 0
                break
    
    result = []
    for k,v in hash_map.items():
        result += v * [k]
    return result




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! Do not give up')    