// 1805. Number of Different Integers in a String
// https://leetcode.com/problems/number-of-different-integers-in-a-string/description/

/**
 * @param {string} word
 * @return {number}
 */

var removeZero = function(array) {
  const result = []
  for(s of array) {
    if(result.length === 0 && s === '0') continue
    result.push(s)
  }
  
  return result.join('')
}
var numDifferentIntegers = function(word) {
  const re = new RegExp(/\d/);
  
  let result = {}
  let stack = []
  
  for(let w of word) {
    if(re.test(w)) {
      stack.push(w)
    } else {
      if(stack.length > 0) result[removeZero(stack)] = true
      stack = []
    }
  }
  
  if(stack.length > 0) result[removeZero(stack)] = true
  
  return Object.keys(result).length
};
