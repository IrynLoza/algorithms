/*
Given an integer n, find the minimal k such that

k = m! (where m! = 1 * 2 * ... * m) for some integer m;
k >= n.
In other words, find the smallest factorial which is not less than n.

Example

For n = 17, the output should be
leastFactorial(n) = 24.

17 < 24 = 4! = 1 * 2 * 3 * 4, while 3! = 1 * 2 * 3 = 6 < 17).
*/

function leastFactorial(n) {
    function factorial(num) {
        let i = 1;
        let result = 1;
        while (i < num) {
            result*= i+1;
            i++;
        };
        return result;
    };
    
    let digit = 1;
    let fact = 1;
    while (digit < n) {
        let curFact = factorial(digit);
        if (curFact < n) {
            fact = curFact;
        } else {
            fact = curFact;
            break;
        }
        digit++;
    }
    return fact; 
}

console.log(leastFactorial(17)) //24
console.log(leastFactorial(1)) //1
console.log(leastFactorial(25)) //120
