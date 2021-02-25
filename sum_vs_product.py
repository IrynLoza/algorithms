"""
Write the function to calculate difference between sum and product of 
array elements:
>>> sum_vs_product([1,2,3,4,5]) 
105
>>> sum_vs_product([2,4,5,15,8]) 
4766
>>> sum_vs_product([1, 1, 1]) 
-2
"""

def sum_vs_product(arr):
    """Return number which represents difference between product and sum"""
    sum_num = arr[0]
    product_num = arr[0]

    for num in arr[1:]:
        sum_num+= num
        product_num*= num

    return product_num - sum_num    




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨Dance with me! ALL TESTS PASS! ✨')



