"""You are given an array items, where each items[i] = [typei, colori, 
namei] describes the type, color, and name of the ith item. You are also 
given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei
>>> count_mathes([["phone","blue","pixel"],["computer","silver","lenovo"], \
["phone","gold","iphone"]], "color", "silver")
1
>>> count_mathes([["phone","blue","pixel"],["computer","silver","phone"], \
["phone","gold","iphone"]], "type", "phone")
2
"""


def count_mathes(items, ruleKey, ruleValue):
    """Return the number of items that match the given rule"""
    key = {
        'type': 0,
        'color': 1, 
        'name': 2
    }
    
    index = key[ruleKey]
        
    result = 0        
    for i in range(len(items)):
        for y in range(len(items[i])):
            if y == index and ruleValue == items[i][y]:
                result+= 1
    return result 




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! Burn it!')