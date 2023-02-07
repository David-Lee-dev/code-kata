// 2265. Count Nodes Equal to Average of Subtree
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/

const VALUE = 0
const COUNT = 1

var averageOfSubtree = function(root) {
  var result = 0
  
  const backOrder = function (node) {
    const leftValueAndCnt = node.left ? backOrder(node.left) : [0, 0]
    const rightValueAndCnt = node.right ? backOrder(node.right) : [0, 0]
    
    const childValueSum = leftValueAndCnt[VALUE] + rightValueAndCnt[VALUE]
    const totalSum = node.val + childValueSum
    const totalCount = 1 + leftValueAndCnt[COUNT] + rightValueAndCnt[COUNT]
    const avg = Math.floor(totalSum / totalCount)
    
    if (avg === node.val) result++;
    
    return [totalSum, totalCount]
  }
  
  backOrder(root)
  
  return result
};
