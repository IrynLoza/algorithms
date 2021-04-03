/*
Ticket numbers usually consist of an even number of digits. A ticket number 
is considered lucky if the sum of the first half of the digits is equal to 
the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
*/

function isLucky(n) {
    let halfSum = 0;
    let string = n.toString();
    let length = Math.round(string.length / 2);
    
    for (let i = 0; i < length; i++) {
        halfSum+= +string[i];
    }
    
    let secondSum = 0;
    for (let i = length; i < string.length; i++) {
        secondSum+= +string[i];
    }
    
    
    return halfSum === secondSum;
}