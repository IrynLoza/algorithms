/*
Every non-negative integer N has a binary representation.  For example, 
5 can be represented as "101" in binary, 11 as "1011" in binary, and so 
on.  Note that except for N = 0, there are no leading zeroes in any binary 
representation.

The complement of a binary representation is the number in binary you get 
when changing every 1 to a 0 and 0 to a 1.  For example, the complement 
of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary 
representation as a base-10 integer.

 

Example 1:

Input: 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, 
which is 2 in base-10.
*/

function bitwiseComplement(N) {
    let binary = N.toString(2);
    let complement = '';
    
    for (let i = 0; i < binary.length; i++) {
        if (binary[i] === '0') {
            complement = `${complement}1`;
        } else {
            complement = `${complement}0`;
        }
    }
    
    let base = 1;
    let result = 0;
    
    for (let i = complement.length-1; i > 0; i--) {
        if (complement[i] === '1') {
            result+= base;
        }
        base*= 2;
    }
    
    return result;
}

console.log(bitwiseComplement(5)) //2
console.log(bitwiseComplement(7)) //0
console.log(bitwiseComplement(10)) //5
