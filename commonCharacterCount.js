/*
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
*/

function commonCharacterCount(s1, s2) {
    let chars = {};
    
    for (let i = 0; i < s1.length; i++) {
        if ( !(s1[i] in chars)) {
            chars[s1[i]] = 1;
        } else {
            chars[s1[i]]++;
        }
    }
    
    let result = 0;
    for (let y = 0; y < s2.length; y++) {
        if (s2[y] in chars && chars[s2[y]] > 0) {
            chars[s2[y]]--;
            result++;
        }
    }
    
    return result;
}