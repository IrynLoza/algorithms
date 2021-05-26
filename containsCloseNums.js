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
    
}

console.log(containsCloseNums([0, 1, 2, 3, 5, 2], 3)); //true
console.log(containsCloseNums([0, 1, 2, 3, 5, 2], 2)); //false
console.log(containsCloseNums([], 0)); //false
console.log(containsCloseNums([0, 1, 2, 3, 4, 0, 0, 7, 8, 9, 10, 11, 12, 0], 1)); //true

