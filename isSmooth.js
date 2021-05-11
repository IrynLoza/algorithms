/*
We define the middle of the array arr as follows:

if arr contains an odd number of elements, its middle is the element whose 
index number is the same when counting from the beginning of the array and 
from its end;
if arr contains an even number of elements, its middle is the sum of the 
two elements whose index numbers when counting from the beginning and from 
the end of the array differ by one.
An array is called smooth if its first and its last elements are equal to 
one another and to the middle. Given an array arr, determine if it is 
smooth or not.
*/

function isSmooth(arr) {

}

console.log(isSmooth([7, 2, 2, 5, 10, 7])); //true
console.log(isSmooth([4, 2])); //false
console.log(isSmooth([-5, -5, 10])); //false
