/*
You are given the root node of a binary search tree (BST) and a value to insert 
into the tree. Return the root node of the BST after the insertion. It is 
guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as 
the tree remains a BST after insertion. You can return any of them.

* Definition for a binary tree node.
* function TreeNode(val, left, right) {
*     this.val = (val===undefined ? 0 : val)
*     this.left = (left===undefined ? null : left)
*     this.right = (right===undefined ? null : right)
* }

* @param {TreeNode} root
* @param {number} val
* @return {TreeNode}

*/

function insertIntoBST(root, val) {
    if (root === null) {
        root = new TreeNode(val);
    //insert to the left subtree    
    } else if (val < root.val) {
        root.left = insertIntoBST(root.left, val);
    //insert to the right subtree
    } else if (val > root.val) {
        root.right = insertIntoBST(root.right, val);
    }

    return root
}