"""An array is monotonic if it is either monotone increasing or monotone 
decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  
An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic:
>>> is_monotonic([1,2,2,3])
True
>>> is_monotonic([6,5,4,4])
True
>>> is_monotonic([1,3,2])
False
>>> is_monotonic([1,1,1])
True
>>> is_monotonic([1,2,4,5])
True
"""

def is_monotonic(A):
    """Return true if array is monotonic"""

    min_num = A[0]
    max_num = A[0]
    
    for num in A[1:]:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    
    if min_num == A[0]:
        i = 0
        while i < len(A)-1:
            if A[i] > A[i+1]:
                return False
            i+= 1
        return True    
        
    elif max_num == A[0]: 
        i = 0
        while i < len(A)-1:
            if A[i] < A[i+1]:
                return False
            i+= 1
        return True




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F Heart guide you! ALL TESTS PASS! Nice job!') 
