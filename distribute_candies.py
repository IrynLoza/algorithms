"""Alice has n candies, where the ith candy is of type candyType[i]. 
Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is 
always even). Alice likes her candies very much, and she wants to eat the 
maximum number of different types of candies while still following the 
doctor's advice.

Given the integer array candyType of length n, return the maximum number 
of different types of candies she can eat if she only eats n / 2 of them:
>>> distribute_candies([1,1,2,2,3,3])
3
>>> distribute_candies([10000,0,10000,0,10000,0,10000,0,10000,0,10000,0,])
2
>>> distribute_candies([6,6,6,6])
1
>>> distribute_candies([1,1,2,3])
2
"""

def distribute_candies(candyType):
    pass



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨Cheers! ALL TESTS PASS! ✨')