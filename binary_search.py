"""Alice has some cards with numbers written on them. She arranges the 
cards in decreasing order, and lays them out face down in a sequence on 
a table. She challenges Bob to pick out the card containing a given number 
by turning over as few cards as possible. Write a function to help Bob 
locate the card:
>>> binary_search([13, 11, 10, 7, 4, 3, 1, 0], 7)
3
>>> binary_search([13, 11, 10, 7, 4, 3, 1, 0], 1)
6
>>> binary_search([4, 2, 1, -1], 4)
0
>>> binary_search([], 7)
-1
>>> binary_search([8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 6)
2
"""
#Helper function to check if element is the first


def binary_search(cards, target):
    """Return index of target card"""

    def direction(cards, target, center):

        mid_point = cards[center]
        if mid_point == target:
            if center-1 >= 0 and cards[center-1] == target:
                return 'left'
            else:
                return 'found' 
        elif mid_point < target:
            return 'left'
        else:
            return 'right'               


    left = 0
    right = len(cards) - 1

    while left < len(cards):
        center = (left+right) // 2
        result = direction(cards, target, center)

        if result == 'found':
            return center
        elif result == 'left':
            right = center - 1
        elif result == 'right':
            left = center + 1
    return -1                 


         








if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Only better forward! ✨')