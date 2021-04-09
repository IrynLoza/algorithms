/*
Write a function that reverses characters in (possibly nested) parentheses 
in the input string.

Input strings will always be well-formed with matching ()s.
*/

function revearseInParentheses(inputString) {
    inputString = inputString.split('');
    let stack = [];
    let temp = [];

    for (let i = 0; i < inputString.length; i++) {
        if (inputString[i] === '(') {
            stack.push(i);
        }
        
        if (inputString[i] === ')') {
            let firstIndex = stack.pop();
            let lastIndex = i;
            temp = inputString.slice(firstIndex, lastIndex + 1);
            temp.reverse();
            inputString.splice(firstIndex, temp.length, ...temp);
            
        } 
    }
    const result = inputString.join('').replace(/[()]/gi, '');
    return result;
}

console.log(revearseInParentheses("(bar)")); // 'rab'
console.log(revearseInParentheses("foo(bar)baz")); // "foorabbaz"
console.log(revearseInParentheses("foo(bar(baz))blim")); // "foobazrabblim"