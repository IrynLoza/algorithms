/*
Consider an arithmetic expression of the form a#b=c. Check whether 
it is possible to replace # with one of the four signs: +, -, * or / to 
obtain a correct expression.
*/

function arithmeticExpression(a, b, c) {
    if (a+b === c || a-b === c || a/b === c || a*b === c) {
        return true;
    } return false;
}

console.log(arithmeticExpression(2, 3, 5)) //true
console.log(arithmeticExpression(8, 2, 4)) //true
console.log(arithmeticExpression(8, 3, 2)) //false