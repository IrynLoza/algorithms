/*
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the 
subtree rooted with that node. If such a node does not exist, return null.
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
 * @param {number} val
 * @return {TreeNode}
 */

function searchBST(root, val) {
    if (root === null) {
        return null
    } 
    if (val === root.val) {
        return root;
    }
    //search in left subtree
    if (val < root.val) {
      return searchBST(root.left, val)
      }
    //search in right subtree    
    if (val > root.val) {
        return searchBST(root.right, val)
    }
}