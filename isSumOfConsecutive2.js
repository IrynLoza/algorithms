/*
Find the number of ways to express n as sum of some (at least two) consecutive positive 
integers.

Example

For n = 9, the output should be
isSumOfConsecutive2(n) = 2.
There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

For n = 8, the output should be
isSumOfConsecutive2(n) = 0.
There are no ways to represent n = 8.
*/

function isSumOfConsecutive2(n) {
    let cur_digit = 1;
    let digit = 1;
    let sum = digit;
    let pair = 0;
    let i = 0;
    
    while (i <= n) {
        while (digit < n) {
            sum = sum + (cur_digit+1);
            if (sum < n) {
                cur_digit++
            } 
            if (sum === n) {
                digit++;
                cur_digit = digit;
                sum = cur_digit;
                pair++;
            }
            if (sum > n) {
                digit++;
                cur_digit = digit;
                sum = cur_digit;
                break;
            }
        }
        i++;
    }
    return pair;
}

console.log(isSumOfConsecutive2(9)) //2
console.log(isSumOfConsecutive2(8)) //0
console.log(isSumOfConsecutive2(8)) //0
console.log(isSumOfConsecutive2(24)) //1
console.log(isSumOfConsecutive2(25)) //2
console.log(isSumOfConsecutive2(880)) //3
