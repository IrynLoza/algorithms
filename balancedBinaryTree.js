/*
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node 
differ in height by no more than 1.
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */

 function isBalanced(root) {
    if (!root) {
        return true;
    }
    
    if (Math.abs(height(root.left)-height(root.right)) > 1) {
        return false;
    } else {
        return isBalanced(root.left) && isBalanced(root.right);
    }
    

    function height(root) {
        if (!root) {
            return 0;
        }
        
        let left = height(root.left);
        let right = height(root.right);
        
        return Math.max(left,right) + 1;
    }  
 }