/**
 Given the root of a binary tree, return the inorder traversal of its nodes' values.
 
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

function inorderTraversal(root: TreeNode | null): number[] {
    if (root === null) {
        return []
    }
    
    let left = inorderTraversal(root.left);
    let key = [root.val];
    let right = inorderTraversal(root.right);
    
    return left.concat(key, right)
};