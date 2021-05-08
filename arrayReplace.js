/*
Given an array of integers, replace all the occurrences of elemToReplace 
with substitutionElem.
*/

function arrayReplace(inputArray, elemToReplace, substitutionElem) {
    for (let i = 0; i < inputArray.length; i++) {
        if (inputArray[i] === elemToReplace) {
           inputArray[i] = substitutionElem;
        }
    }
    return inputArray;
}

console.log(arrayReplace([1,2,1], 1, 3)); //[3,2,3]
console.log(arrayReplace([1, 2, 3, 4, 5], 3, 0)); //[1, 2, 0, 4, 5]
console.log(arrayReplace([1, 2, 1, 2, 1], 2, 2)); //[1, 2, 1, 2, 1]
