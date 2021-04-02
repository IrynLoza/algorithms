/**
Given the root of a binary tree, return the postorder traversal of its nodes' values.

 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function postorderTraversal(root: TreeNode | null): number[] {
    if (root === null) {
        return []
    }
    
    let left = postorderTraversal(root.left);
    let key = [root.val];
    let right = postorderTraversal(root.right);
    
    return left.concat(right, key);
};