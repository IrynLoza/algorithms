/*
We define the middle of the array arr as follows:

if arr contains an odd number of elements, its middle is the element 
whose index number is the same when counting from the beginning of the 
array and from its end;
if arr contains an even number of elements, its middle is the sum of the 
two elements whose index numbers when counting from the beginning and from 
the end of the array differ by one.
Given array arr, your task is to find its middle, and, if it consists of 
two elements, replace those elements with the value of middle. Return the 
resulting array as the answer.

Example
For arr = [7, 2, 2, 5, 10, 7], the output should be
replaceMiddle(arr) = [7, 2, 7, 10, 7].

The middle consists of two elements, 2 and 5. These two elements should 
be replaced with their sum, i.e. 7.

For arr = [-5, -5, 10], the output should be
replaceMiddle(arr) = [-5, -5, 10].
*/

function replaceMiddle(arr) {
    let middle = 0;
        
    if (arr.length%2 === 0) {
        let index = arr.length/2;
        middle = arr[index] + arr[index-1];
        arr.splice(index-1, 2, middle);     
    }
    return arr;
}

console.log(replaceMiddle([7, 2, 2, 5, 10, 7])) //[7, 2, 7, 10, 7]
console.log(replaceMiddle([-5, -5, 10])) //[-5, -5, 10]
console.log(replaceMiddle([9, 0, 15, 9])) //[9, 15, 9]

