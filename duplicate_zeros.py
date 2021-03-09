"""Given a fixed length array arr of integers, duplicate each occurrence of zero, 
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place:
>>> duplicate_zeros([1,0,2,3,0,4,5,0])
[1, 0, 0, 2, 3, 0, 0, 4]
>>> duplicate_zeros([1,2,3])
[1, 2, 3]
"""

def duplicate_zeros(arr):
    """Return array with duplicate zeros"""
    length = len(arr)
    i = 0
    while i < length:
        if arr[i] == 0:
            arr.insert(i, 0)
            i+= 2
            arr.pop()
        else:
            i+= 1

    return arr        




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F \u2764\uFE0F \u2764\uFE0F ALL TESTS PASS! \
               Love with you! \u2764\uFE0F \u2764\uFE0F \u2764\uFE0F')