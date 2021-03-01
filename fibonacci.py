"""The Fibonacci numbers, commonly denoted F(n) form a sequence, called the 
Fibonacci sequence, such that each number is the sum of the two preceding ones, 
starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
>>> fib(2)
1
>>> fib(3)
2
>>> fib(4)
3
"""

def fib(n):
    """Return fibonacci of n"""
    
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)   




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! Amazing job!') 