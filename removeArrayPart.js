/*
Remove a part of a given array between given 0-based indexes 
l and r (inclusive).
*/

function removeArrayPart(inputArray, l, r) {
    let num = (r-l);
    inputArray.splice(l, num+1);
    
    return inputArray;
}

console.log(removeArrayPart([2, 3, 2, 3, 4, 5], 2, 4)); // [2,3,5]
console.log(removeArrayPart([2, 4, 10, 1], 0, 2)); // [1]
console.log(removeArrayPart([1, 1], 0, 1)); // []