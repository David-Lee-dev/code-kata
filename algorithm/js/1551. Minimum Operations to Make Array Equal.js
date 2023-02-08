// 1551. Minimum Operations to Make Array Equal
// https://leetcode.com/problems/minimum-operations-to-make-array-equal/description/


var minOperations = function(n) {
  var result = 0
  for(i=1; i<=Math.floor(n/2); i++) {
    const a = (2 * i) - 1
    const b = (2 * (n - i)) + 1
    result += (b - a) / 2
  }
  
  return result
};
