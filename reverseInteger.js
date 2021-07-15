/*
Reverse the digits of the given integer.
*/

function reverseInteger(x) {
    const string = x.toString().split('');
    let result = [];
    if (string[0] === '-') {
        result.push('-');
        string.splice(0, 1);
    }
    
    for (let i = string.length-1; i >= 0; i--) {
        result.push(string[i]);
    }
    const arr = result.join('');
    
    return +arr;
};

console.log(reverseInteger(12345)) //54321
console.log(reverseInteger(-98765)) //-56789