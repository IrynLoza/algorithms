"""Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]":
>>> defanging_ip("1.1.1.1")
'1[.]1[.]1[.]1'
>>> defanging_ip("255.100.50.0")
'255[.]100[.]50[.]0'
"""

def defanging_ip(address):
    """Return defanged IP address"""
    result = ""
        
    for char in address:
        if char != '.':
            result = f"{result}{char}"
        else:
            result = f"{result}["
            result = f"{result}{char}"
            result = f"{result}]"
    return result 




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨ALL TESTS PASS! Who is good girl? You are! ✨')