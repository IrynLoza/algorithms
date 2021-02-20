"""
Convert the date string to the format YYYY-MM-DD:
>>> reformat_date("20th Oct 2052")
"2052-10-20"
>>> reformat_date("6th Jun 1933")
"1933-06-06"
>>> reformat_date("26th May 1960")
"1960-05-26"
"""

def reformat_date(date):
    pass




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TEST PASS! You are stronger every day!')
