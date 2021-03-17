"""Alice has some cards with numbers written on them. She arranges the 
cards in decreasing order, and lays them out face down in a sequence on 
a table. She challenges Bob to pick out the card containing a given number 
by turning over as few cards as possible. Write a function to help Bob 
locate the card:
>>> binary_search([13, 11, 10, 7, 4, 3, 1, 0], 3)
3
>>> binary_search([13, 11, 10, 7, 4, 3, 1, 0], 1)
6
>>> binary_search([4, 2, 1, -1], 4)
0
>>> binary_search([], 7)
-1
>>> binary_search([8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 6)
6
"""

def binary_search(cards, target):
    """Return index of target card"""
    







if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Only better forward! ✨')