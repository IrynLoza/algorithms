/*
Given an integer num, return a string of its base 7 representation.
*/

function base7(num) {
    return num.toString(7);
};

console.log(base7(100)); //'202'
console.log(base7(-7)); //'-10'