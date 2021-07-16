/*
You are supposed to label a bunch of boxes with numbers from 0 to n, 
and all the labels are stored in the array arr. Unfortunately one of 
the labels is missing. Your task is to find it.
*/

function missingNumber(arr) {
    let sum = arr.length;
    for (let i = 0; i < arr.length; i++) {
        sum += i - arr[i];
    };

    return sum;
};

console.log(missingNumber([3,1,0])) //2
console.log(missingNumber([0])) //1
console.log(missingNumber([5, 2, 1, 6, 3, 0])) //4


