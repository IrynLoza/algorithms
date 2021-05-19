/*
Determine if the given number is a power of some non-negative integer.
*/

function isPower(n) {
    if (n < 2) {
        return true;
    }
    
    let digit = 2;
    let pow = digit;
    
    while (digit < n) {
        while (pow !== n) {
            pow = pow*digit;
            if (pow > n) {
                digit++;
                pow = digit;
                break;
            }
            if (pow === n) {
                return true;
            }
        }
    }
    return false;
    
}

console.log(isPower(125)) //true
console.log(isPower(72)) //false
console.log(isPower(11)) //false
console.log(isPower(1)) //true
console.log(isPower(256)) //true
