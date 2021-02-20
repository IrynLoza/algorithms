"""
Convert the date string to the format YYYY-MM-DD:
>>> reformat_date("20th Oct 2052")
'2052-10-20'
>>> reformat_date("6th Jun 1933")
'1933-06-06'
>>> reformat_date("26th May 1960")
'1960-05-26'
"""

def reformat_date(date):
    "Return converted date"

    date = date.split(' ')
    devicer = '-'
    result = ''
    zero = '0'
    
    months = {
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12',
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08' 
    }
    
    for i in range(len(date)-1, -1, -1):
        if date[i] in months:
            result = f'{result}{months[date[i]]}{devicer}'
        elif date[i].isdigit() == False and date[i].isalpha() == False:
            if len(date[i]) > 3:
                result = f'{result}{date[i][:2]}'
            else:
                result = f'{result}{zero}{date[i][:1]}'
        else:
            result = f'{result}{date[i]}{devicer}'    
    return result




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n \u2764\uFE0F ALL TEST PASS! You are stronger every day!')
