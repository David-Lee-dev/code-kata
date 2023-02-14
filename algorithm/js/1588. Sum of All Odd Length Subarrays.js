// 1588. Sum of All Odd Length Subarrays
// https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/

/**
 * @param {number[]} arr
 * @return {number}
 */
var summary = function (nums) {
  let result = 0
  
  for(n of nums) result += n
  
  return result
}

var sumOddLengthSubarrays = function(arr) {
  let result = 0
  
  for(let length = 1; length <= arr.length; length++) {
    if(length % 2 === 0) continue
    
    for(let idx = 0; idx < arr.length - length + 1; idx++) {
      const tmp = arr.slice(idx, idx + length)
      result += summary(tmp)
    }
  }
  
  return result
};
