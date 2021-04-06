/*
Given a string s consisting of small English letters, find and return the 
first instance of a non-repeating character in it. If there is no such 
character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since 
it appears in the string first.
*/

function firstNotRepeatingCharacter(s) {
    let hash_map = {};
    
    for (let char of s) {
        if (char in hash_map) {
            hash_map[char] = false;
        } else {
            hash_map[char] = true;
        }
    }
    
    if (Object.values(hash_map).includes(true)) {
        let index = s.length;
        for (let i = 0; i < s.length; i++) {
            if (hash_map[s[i]] === true) {
                if (i < index) {
                    index = i;
                }
            } 
        }
        return s[index];
    } else {
        return '_';
    }  
}

console.log(firstNotRepeatingCharacter("abacabad")) //'c'
console.log(firstNotRepeatingCharacter("abacabaabacaba")) //'_'