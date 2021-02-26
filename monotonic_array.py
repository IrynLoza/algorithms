"""An array is monotonic if it is either monotone increasing or monotone 
decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  
An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic:
>>> monotonic_array([1,2,2,3])
true
>>> monotonic_array([6,5,4,4])
true
>>> monotonic_array([1,3,2])
false
>>> monotonic_array([1,1,1])
true
>>> monotonic_array([1,2,4,5])
true
"""

def monotonic_array(A):
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F Heart guide you! ALL TESTS PASS! Nice job!') 
