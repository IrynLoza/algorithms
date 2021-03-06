"""You are given an m x n integer grid accounts where accounts[i][j] is the 
amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that 
the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.
>>> richest_customer([[1,2,3],[3,2,1]])
6
>>> richest_customer([[1,5],[7,3],[3,5]])
10
"""

def richest_customer(accounts):
    """Return wealth of richest customer"""
    max_wealth = 0
        
    for i in range(len(accounts)):
        wealth = 0
        for y in range(len(accounts[i])):
            wealth+= accounts[i][y]
        if wealth > max_wealth:
            max_wealth = wealth
        
    return max_wealth 




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
         print('\n \u2764\uFE0F ALL TESTS PASS! Keep going! \u2764\uFE0F')