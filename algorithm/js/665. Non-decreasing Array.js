// 665. Non-decreasing Array
// https://leetcode.com/problems/non-decreasing-array/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var checkPossibility = function(nums) {
  let cnt = 0
  for(let i=nums.length - 1; i > 0; i--){
    if(nums[i]< nums[i - 1]){
      if(nums[i-1] > nums[i + 1]) nums[i - 1] = nums[i]
      else nums[i] = nums[i - 1]
      cnt++
      
      if(i < nums.length - 1 && nums[i] > nums[i+1]) return false
    }
    
    if(cnt > 1) return false
  }
  
  return true
};
