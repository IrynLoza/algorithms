/*
You are given a two-digit integer n. Return the sum of its digits.
*/

function addTwoDigits(n) {
    n = n.toString();
    return +n[0]+(+n[1])
}
console.log(addTwoDigits(29)) //11
console.log(addTwoDigits(32)) //5
