// 1261. Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/

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
 */

var FindElements = function(root) {
  this.root = root
  
  if(root.val === -1) root.val = 0
  
  if(root.left !== null) {
    root.left.val = 2 * root.val + 1
    FindElements(root.left)
  }
  if(root.right !== null) {
    root.right.val = 2 * root.val + 2
    FindElements(root.right)
  }
};

/**
 * @param {number} target
 * @return {boolean}
 */
FindElements.prototype.find = function(target) {
  var result = false
  var recursion = function(node) {
    if(node.val === target) {
      result = true
      return
    }
    
    if(node.left) recursion(node.left)
    if(node.right) recursion(node.right)
  }
  
  recursion(this.root)
  return result
};

/**
 * Your FindElements object will be instantiated and called as such:
 * var obj = new FindElements(root)
 * var param_1 = obj.find(target)
 */
