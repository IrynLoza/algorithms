/*
Given an array a that contains only numbers in the range from 1 to a.length, 
find the first duplicate number for which the second occurrence has the minimal 
index. In other words, if there are more than 1 duplicated numbers, return the 
number for which the second occurrence has a smaller index than the second 
occurrence of the other number does. If there are no such elements, return -1.

Example

For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller 
index than the second occurrence of 2 does, so the answer is 3.

For a = [2, 2], the output should be firstDuplicate(a) = 2;

For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1.

The element in a that occurs in the array more than once and has the minimal 
index for its second occurrence. If there are no such elements, return -1.
*/

function firstDuplicate(a) {
    let hash_map = {};
    let maxLength = 0;
    
    for (let i = 0; i < a.length; i++) {
        if (a[i] in hash_map) {
            hash_map[a[i]].push(i);
            if (hash_map[a[i]].length > maxLength) {
                maxLength = hash_map[a[i]].length;
            }
        } else {
            hash_map[a[i]] = [i];
        }
    }
    
    if (maxLength === 0) {
        return -1;
    } else {
        let minLastIndex = a.length;

        for (key in hash_map) {
            if (hash_map[key].length === maxLength) {
                if (hash_map[key][hash_map[key].length-1] < minLastIndex) {
                    minLastIndex = hash_map[key][hash_map[key].length-1]
                }
            }
        }
        return a[minLastIndex];
        }
}

console.log(firstDuplicate([2, 1, 3, 5, 3, 2])) //3
console.log(firstDuplicate([2, 4, 3, 5, 1])) //-1
console.log(firstDuplicate([2, 2])) //2