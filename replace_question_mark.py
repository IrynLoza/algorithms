"""Given a string s containing only lower case English letters and the '?' character, 
convert all the '?' characters into lower case letters such that the final string does 
not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string 
except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there 
is more than one solution, return any of them. It can be shown that an answer is always possible 
with the given constraints:
"""

def replace_question_mark(s):
    """Return string with replaced question marks"""
    pass

print(replace_question_mark('?zs'))
"""There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" 
is an invalid modification as the string will consist of consecutive repeating characters in "zzs"""
print(replace_question_mark('ubv?w'))
print(replace_question_mark('??yw?ipkj?'))
