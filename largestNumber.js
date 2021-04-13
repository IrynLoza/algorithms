/*
Given an integer n, return the largest number that contains exactly n digits.
*/

function largestNum(n) {
    let i = n;
    let result = '';
    while (i > 0) {
        result = `${result}9`;
        i--;
    }
    
    return +result
}

console.log(largestNum(2)) // 99
console.log(largestNum(3)) // 999
