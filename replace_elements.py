"""Given an array arr, replace every element in that array with the 
greatest element among the elements to its right, and replace the last 
element with -1:
>>> replaced([17,18,5,4,6,1])
[18, 6, 6, 6, 1, -1]
>>> replaced([400])
[-1]
"""

def replaced(arr):
    """Return array with replaced numbers"""
    result = []
        
    for i in range(len(arr)):
        max_num = arr[i:][0]
        for num in arr[i:]:
            if num > max_num:
                max_num = num
        result.append(max_num)  
    return result[1:] + [-1]




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Only better forward! ✨')