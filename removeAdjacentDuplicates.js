/*
Given a string S of lowercase letters, a duplicate removal consists of choosing 
two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is 
guaranteed the answer is unique.
*/

function removeAdjacentDuplicates(S) {
    let stack = [S[0]];
    
    for (let i = 1; i < S.length; i++) {
        if (stack[stack.length-1] !== S[i]) {
            stack.push(S[i]);
        } else {
            stack.pop();
        }
    }
    
    return stack.join('');
};

console.log(removeAdjacentDuplicates("abbaca")); // 'ca'
