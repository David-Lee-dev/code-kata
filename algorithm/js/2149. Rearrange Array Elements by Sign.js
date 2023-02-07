// 2149. Rearrange Array Elements by Sign
// src: https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

var rearrangeArray = function(nums) {
  const result = new Array(nums.length)
  let nxtPosIdx = 0
  let nxtNegIdx = 1
  
  for(let i=0; i< nums.length; i++) {
    if(nums[i] > 0) {
      result[nxtPosIdx] = nums[i]
      nxtPosIdx += 2
    } else {
      result[nxtNegIdx] = nums[i]
      nxtNegIdx += 2
    }
  }
  
  return result
};
