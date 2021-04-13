/*
Given an array arr of positive integers sorted in a strictly increasing order, 
and an integer k.

Find the kth positive integer that is missing from this array.
*/

function kthMissing(arr, k) {
    let missing = [];
    let curDigit = 1;
    i = 0
    while (missing.length < k) {
        if (arr[i] === curDigit) {
            i++
            curDigit++
        } else {
            missing.push(curDigit)
            curDigit++
        }
    }
    
    return missing[missing.length-1]
}

console.log(kthMissing([2,3,4,7,11], 5)) // 9
console.log(kthMissing([1,2,3,4], 2)) // 6