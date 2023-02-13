// 75. Sort Colors
// https://leetcode.com/problems/sort-colors/description/

var sortColors = function(nums) {
  let i = 0;
  
  while(i < nums.length) {
    console.log(i, nums)
    if(nums[i] === 0) {
      for(let j=0; j<i; j++) {
        if(nums[j] > 0) {
          const tmp = nums[j]
          nums[j] = nums[i]
          nums[i] = tmp
          
          if(nums[j] === 1) {
            i++
          } else {
            i--
          }
          break
        }
      }
    }else if (nums[i] === 2) {
      for(let j=nums.length - 1; j>i; j--) {
        if(nums[j] < 2) {
          const tmp = nums[j]
          nums[j] = nums[i]
          nums[i] = tmp
          
          if(nums[j] === 1) {
            i++
          } else {
            i--
          }
          break
        }
        
      }
    }
    i++
  }
};
