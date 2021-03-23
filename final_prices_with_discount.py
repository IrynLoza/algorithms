"""Given the array prices where prices[i] is the price of the ith item in a 
shop. There is a special discount for items in the shop, if you buy the ith 
tem, then you will receive a discount equivalent to prices[j] where j is the 
minimum index such that j > i and prices[j] <= prices[i], otherwise, you will 
not receive any discount at all.

Return an array where the ith element is the final price you will pay for the 
ith item of the shop considering the special discount:
>>> final_prices([8,4,6,2,3])
[4, 2, 4, 2, 3]
>>> final_prices([1,2,3,4,5])
[1, 2, 3, 4, 5]
"""

def final_prices(prices):
    """Return array with final prices"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Nice Iryn! ✨')