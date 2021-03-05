"""
There is a restaurant with a single chef. You are given an array customers, 
where customers[i] = [arrivali, timei]:

arrivali is the arrival time of the ith customer. The arrival times are sorted 
in non-decreasing order.
timei is the time needed to prepare the order of the ith customer.
When a customer arrives, he gives the chef his order, and the chef starts 
preparing it once he is idle. The customer waits till the chef finishes 
preparing his order. The chef does not prepare food for more than one customer 
at a time. The chef prepares food for customers in the order they were given in 
the input.

Return the average waiting time of all customers. Solutions within 10-5 from the 
actual answer are considered accepted:
>>> average_time([[1,2],[2,5],[4,3]])
5.00000
>>> average_time([[5,2],[5,4],[10,3],[20,1]])
3.25000
"""

def average_time(customers):
    """Return the average waiting time of all customers"""
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! You are great, hah? \u2764\uFE0F')