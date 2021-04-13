/*
Given an array of integers, find the maximal absolute difference
 between any two of its adjacent elements.
*/

function arrayMaximalAdjacentDifference(inputArray) {
    let value = 0;
    for (let i = 0; i < inputArray.length; i++) {
        let diff = 0;
        diff = Math.max((inputArray[i]-inputArray[i+1]), (inputArray[i+1]-inputArray[i]))
        if (diff > value) {
            value = diff;
        }
    }
    return value;
}

console.log(arrayMaximalAdjacentDifference([2, 4, 1, 0])) //3
console.log(arrayMaximalAdjacentDifference([10, 11, 13])) //2
console.log(arrayMaximalAdjacentDifference([-2, -2, -2, -2, -2])) //0
console.log(arrayMaximalAdjacentDifference([-1, 1, -3, -4])) //4
