/*
Given a character, check if it represents an odd digit, an even digit or 
not a digit at all.

Example

For symbol = '5', the output should be
characterParity(symbol) = "odd";
For symbol = '8', the output should be
characterParity(symbol) = "even";
For symbol = 'q', the output should be
characterParity(symbol) = "not a digit".
*/

function characterParity(symbol) {
    const odd = 'odd';
    const even = 'even';
    const notADigit = 'not a digit';
    
    if (isNaN(+symbol)) {
        return notADigit;
    } else if (+symbol%2 !== 0) {
        return odd;
    } else if (+symbol%2 === 0) {
        return even;
    } 
};

console.log(characterParity('8')) //even
console.log(characterParity('5')) //odd
console.log(characterParity('q')) //not a digit