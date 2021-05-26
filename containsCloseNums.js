/*
Given an array of integers nums and an integer k, determine whether there are two 
distinct indices i and j in the array where nums[i] = nums[j] and the absolute 
difference between i and j is less than or equal to k.

Example:

For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
containsCloseNums(nums, k) = true.

There are two 2s in nums, and the absolute difference between their positions is exactly 3.
For nums = [0, 1, 2, 3, 5, 2] and k = 2, the output should be
containsCloseNums(nums, k) = false.
*/

function containsCloseNums(nums, k) {
    let flag = false;
    hashMap = {}
    
    for (let i = 0; i < nums.length; i++) {
        if (!(nums[i] in hashMap)) {
            hashMap[nums[i]] = [i];
        } else {
            hashMap[nums[i]].push(i);
        }
    }

    for (let key in hashMap) {
        if (hashMap[key].length >= 2) {
            for (let j = 0; j < hashMap[key].length-1; j++) {
                if (hashMap[key][j+1] - hashMap[key][j] <= k) {
                    return true;
                } else {
                    flag = false;
                }
            }
        } 
    }
    return flag;
}

console.log(containsCloseNums([0, 1, 2, 3, 5, 2], 3)); //true
console.log(containsCloseNums([0, 1, 2, 3, 5, 2], 2)); //false
console.log(containsCloseNums([], 0)); //false
console.log(containsCloseNums([0, 1, 2, 3, 4, 0, 0, 7, 8, 9, 10, 11, 12, 0], 1)); //true

