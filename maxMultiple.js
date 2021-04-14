/*
Given a divisor and a bound, find the largest integer N such that:

N is divisible by divisor.
N is less than or equal to bound.
N is greater than 0.
It is guaranteed that such a number exists.
*/

function maxMultiple(divisor, bound) {
    let number = 0;
    
    let i = bound;
    while (i > 0) {
        if (i%divisor === 0) {
            if (i > number) {
                number = i;
            } else {
                break;
            }
        }
        i--
    }
    
    return number;
}

console.log(maxMultiple(3, 10)) //9
console.log(maxMultiple(7, 100)) //98