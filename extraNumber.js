/*
You're given three integers, a, b and c. It is guaranteed that 
two of these integers are equal to each other. What is the value 
of the third integer?
*/

function extraNumber(a, b, c) {
    if (a === c) {
        return b;
    } else if (b === c) {
        return a;
    } else if (a === b) {
        return c;
    };
};

console.log(extraNumber(2,7,2)); //7
console.log(extraNumber(5,5,2)); //2
console.log(extraNumber(4,2,2)); //4