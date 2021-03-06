/*
You are given two integer arrays nums1 and nums2 both of unique elements, 
where nums1 is a subset of nums2.

Find all the next greater numbers for nums1's elements in the corresponding 
places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to 
its right in nums2. If it does not exist, return -1 for this number.
*/

function nextGreater(nums1, nums2) {
    let result = [];
    for (let i = 0; i < nums1.length; i++) {
        result.push(-1);
        let target = nums1[i];
        let index = nums2.indexOf(nums1[i]);
        let temp = nums2.slice(index, nums2.length);
        y = 0;
        
        while (y < temp.length) {
            if (temp[y] > target) {
                result.pop();
                result.push(temp[y]);
                break;
            } 
            
            y++;   
        }
    }
    return result;
};

console.log(nextGreater([4,1,2], [1,3,4,2])) // Output: [-1,3,-1]
console.log(nextGreater([2,4], [1,2,3,4])) // [3, -1]
