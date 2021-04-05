/*
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the 
root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5


* Definition for a binary tree node.
* function TreeNode(val, left, right) {
*     this.val = (val===undefined ? 0 : val)
*     this.left = (left===undefined ? null : left)
*     this.right = (right===undefined ? null : right)
* }
@param {TreeNode} root
@return {number}
*/

function minDepth(root) {
    if (root === null) {
        return 0;
    }
    
    if (root.left === null) {
        return 1 + minDepth(root.right);
    } else if (root.right === null) {
        return 1 + minDepth(root.left);
    } else {
        return 1 + Math.min(minDepth(root.right), minDepth(root.left));
    }
}