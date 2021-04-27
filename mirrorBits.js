/*
Reverse the order of the bits in a given integer.

Example:
For a = 97, the output should be
mirrorBits(a) = 67.

97 equals to 1100001 in binary, which is 1000011 after mirroring, 
and that is 67 in base 10.

For a = 8, the output should be
mirrorBits(a) = 1.
*/

function mirrorBits(a) {
    let binaryNum = a.toString(2);
    
    let reversed = '';
    for (let i = binaryNum.length-1; i >= 0; i--) {
        reversed = `${reversed}${binaryNum[i]}`
    };
    
    let result = 0;
    base = 1;
    for (let i = reversed.length-1; i >= 0; i--) {
        if (reversed[i] === '1') {
            result+= base;
        };
        base*= 2;
    }
    
    return result;
};

console.log(mirrorBits(97)) // 67
console.log(mirrorBits(86782)) // 65173
console.log(mirrorBits(8)) // 1


