/*
Write a function that reverses characters in (possibly nested) parentheses 
in the input string.

Input strings will always be well-formed with matching ()s.
*/

function revearseInParentheses(inputString) {

}

console.log(revearseInParentheses("(bar)")); // 'rab'
console.log(revearseInParentheses("foo(bar)baz")); // "foorabbaz"
console.log(revearseInParentheses("foo(bar(baz))blim")); // "foobazrabblim"