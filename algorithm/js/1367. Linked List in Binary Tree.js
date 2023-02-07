// 1367. Linked List in Binary Tree
// https://leetcode.com/problems/linked-list-in-binary-tree/description/
var isSubPath = function(head, root) {
  if(!root)    return false
  if(issame(head, root))  return true
  return isSubPath(head, root.left) || isSubPath(head, root.right)
};

function issame(nodeOfList, nodeOfTree){
  if(!nodeOfList)   return true
  if(!nodeOfTree)   return false
  if(nodeOfList.val != nodeOfTree.val)    return false
  return issame(nodeOfList.next, nodeOfTree.left) || issame(nodeOfList.next, nodeOfTree.right)
};
