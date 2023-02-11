// 1669. Merge In Between Linked Lists
// https://leetcode.com/problems/merge-in-between-linked-lists/description/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {number} a
 * @param {number} b
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeInBetween = function(list1, a, b, list2) {
  var find = function (node) {
    while(node.next) node = node.next
    
    return node
  }
  var insert = function (node, count) {
    if(node.next === null) return
    if(count === a - 1) {
      const tmp = node.next
      node.next = list2
      insert(tmp, count + 1)
      return
    }
    if(count === b) {
      const last = find(list2)
      last.next = node.next
      return
    }
    insert(node.next, count + 1)
  }
  insert(list1, 0)
  
  return list1
};
