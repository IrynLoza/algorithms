/*
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1]
is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its 
traversing-order next in the array, which means you could search circularly to 
find its next greater number. If it doesn't exist, return -1 for this number.
*/

function nextGreaterElements(nums) {
    let stack = [];
 
    for (let i = 0; i < nums.length; i++) {
        stack.push(-1);
        
        let temp = nums.slice(i, nums.length).concat(nums.slice(0, i));
        y = 0;
        while (y < temp.length) {
            if (temp[y] > nums[i]) {
                stack.pop();
                stack.push(temp[y]);
                break;
            } 
            y++;
        }   
    };
    
    return stack
}

console.log(nextGreaterElements([1,2,1])); //[2,-1,2]
console.log(nextGreaterElements([1,2,3,4,3])); //[2,3,4,-1,4]