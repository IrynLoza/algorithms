/* 
Given a string, find out if its characters can be rearranged to form a palindrome.
*/

function isPalindrome(inputString) {
    let count = 0;
    let hash_map = {};
    
    for (let i = 0; i < inputString.length; i++) {
        if (inputString[i] in hash_map) {
            hash_map[inputString[i]]++;
        } else {
            hash_map[inputString[i]] = 1;
        }
    }
    
    for (let key in hash_map) {
        if (hash_map[key]%2 !== 0) {
            count++;
        }
    }
    
    if (count > 1) {
        return false;
    } else {
        return true;
    }
}

console.log(isPalindrome('aabb')) //true
console.log(isPalindrome('zyyzzzzz')) //true
console.log(isPalindrome('abca')) //false

