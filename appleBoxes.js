/* 
You have k apple boxes full of apples. Each square box of size m contains
 m × m apples. You just noticed two interesting properties about the boxes:

The smallest box is size 1, the next one is size 2,..., all the way up to 
size k.
Boxes that have an odd size contain only yellow apples. Boxes that have an 
even size contain only red apples.
Your task is to calculate the difference between the number of red apples 
and the number of yellow apples.

Example

For k = 5, the output should be
appleBoxes(k) = -15.

There are 1 + 3 * 3 + 5 * 5 = 35 yellow apples
2 * 2 + 4 * 4 = 20 red apples, 
making the answer 20 - 35 = -15.
*/

function appleBoxes(k) {
    let yellow = 0;
    let red = 0;
    
    while (k !== 0) {
        if (k%2 === 0) {
            red+= k*k;
        } else {
            yellow+= k*k;
        }
        k--;
    }
    
    return red-yellow;
}

console.log(appleBoxes(5)) // -15
console.log(appleBoxes(36)) // 666
console.log(appleBoxes(0)) // 0