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
5.0
>>> average_time([[5,2],[5,4],[10,3],[20,1]])
3.25
"""

def average_time(customers):
    """Return the average waiting time of all customers"""
    arrival = customers[0][0]
    first_time = customers[0][1]
    time = arrival + first_time
    count_time = time - arrival
    for i in range(1, len(customers)):
        #if time greater then arrival of next customer 
        #increase time by next customer time 
        if time > customers[i][0]:
            time += customers[i][1]
            #increase count_time
            count_time += time - customers[i][0]
        else: 
            #if next customer arrive letter the previous and time less
            #then arrival -> increase count time by next customer time
            #and update time with 'first customer formula' 
            count_time += customers[i][1]
            time = customers[i][0] + customers[i][1]
    return count_time/len(customers)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! You are great, hah? \u2764\uFE0F')