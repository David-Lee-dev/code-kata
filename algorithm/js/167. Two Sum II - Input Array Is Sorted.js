// 167. Two Sum II - Input Array Is Sorted
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

var twoSum = function(numbers, target) {
  for(let first=0; first< numbers.length-1; first++) {
    for(let second=first + 1; second<numbers.length; second++) {
      const total = numbers[first] + numbers[second]
      
      if(total > target) break
      if(total === target) return [first + 1, second + 1]
    }
  }
};
