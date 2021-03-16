"""Given an array of integers arr, write a function absSort(arr), that sorts 
the array according to the absolute values of the numbers in arr. If two 
numbers have the same absolute value, sort them according to sign, where the 
negative numbers come before the positive numbers:
>>> abs_sort([2, -7, -2, -2, 0])
[0, -2, -2, 2, -7]
>>> abs_sort([-2,1])
[1, -2]
>>> abs_sort([-2,3,5,-1,4])
[-1, -2, 3, 4, 5]
"""

def abs_sort(arr):
    """Return sorted array in absolute order
    
    Write a custom comparison function, such as smaller(a, b) which 
    is true if and only if a is supposed to come before b (and a != b). 
    From here, we can repeatedly find the ‘smallest’ number in A[i], 
    A[i+1], ..., A[A.length - 1] and swapping it with A[i].
    """

    def smaller(a, b):
        """Find smaller num in absolute"""
        if abs(a) < abs(b):
            return True
        elif abs(a) > abs(b):
            return False
        return a < b
    
    for i in range(len(arr)):
        best = i
        for y in range(i, len(arr)):
            if smaller(arr[y], arr[best]):
                best = y
        arr[best], arr[i] = arr[i], arr[best]   
    return arr
    




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TESTS PASS! You did it!')
