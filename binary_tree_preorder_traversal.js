/**
 Given the root of a binary tree, return the preorder traversal of its nodes' values.
 
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

function preorderTraversal(root: TreeNode | null): number[] {
    if (root === null) {
        return []
    }
    
    let key = [root.val];
    let left = preorderTraversal(root.left);
    let right = preorderTraversal(root.right);
    
    return key.concat(left, right)
};