/*
We want to turn the given integer into a number that has only one non-zero 
digit using a tail rounding approach. This means that at each step we take
 the last non 0 digit of the number and round it to 0 or to 10. If it's 
 less than 5 we round it to 0 if it's larger than or equal to 5 we round 
 it to 10 (rounding to 10 means increasing the next significant digit by 1). 
 The process stops immediately once there is only one non-zero digit left.

Example
For n = 15, the output should be
rounders(n) = 20;

For n = 1234, the output should be
rounders(n) = 1000.
1234 -> 1230 -> 1200 -> 1000.
*/

function rounders(n) {
    let num = n.toString();
    let converted = '';
    let add = 0;
    let number = 0;
    
    for (let i = num.length; i >= 0; i--) {
        if (num[i] < 5 && i > 0) {
            converted  = `0${converted}`;
        } else if (num[i] >= 5 && i > 0) {
            add = 1;
            converted = `0${converted}`;
        } else if (i === 0 && add > 0) {
            number = +num[i] + 1;
            converted = `${number}${converted}`
        } else if (i === 0 && add < 1) {
            converted = `${num[i]}${converted}`
        } 
    }    

    return +converted;
}

console.log(rounders(15)) //20
console.log(rounders(1234)) //1000
console.log(rounders(99)) //100