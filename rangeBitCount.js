/*
You are given two numbers a and b where 0 ≤ a ≤ b. Imagine you 
construct an array of all the integers from a to b inclusive. 
You need to count the number of 1s in the binary representations 
of all the numbers in the array.

Example:
For a = 2 and b = 7, the output should be
rangeBitCount(a, b) = 11.

Given a = 2 and b = 7 the array is: [2, 3, 4, 5, 6, 7]. Converting 
the numbers to binary, we get [10, 11, 100, 101, 110, 111], which 
contains 1 + 2 + 1 + 2 + 2 + 3 = 11 1s.
*/

function rangeBitCount(a, b) {
    let i = 0;
    let nums = [];
    while (i <= b) {
        if (i >= a) {
            nums.push(i)
        };
        i++;
    }
    
    let result = 0;
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i];
        //COnver to binary (with base 2)
        let binary = (num).toString(2);
        let sum = 0;
        for (let y = 0; y < binary.length; y++) {
            sum+= +binary[y];
        }
        result+= sum;
        sum = 0;
    }
    
    return result;
}

console.log(rangeBitCount(2, 7)) // 11
console.log(rangeBitCount(0, 1)) // 1
console.log(rangeBitCount(9, 10)) // 4