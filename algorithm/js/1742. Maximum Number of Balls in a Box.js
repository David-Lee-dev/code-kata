// 1742. Maximum Number of Balls in a Box
// https://leetcode.com/problems/maximum-number-of-balls-in-a-box/description/

/**
 * @param {number} lowLimit
 * @param {number} highLimit
 * @return {number}
 */
var countBalls = function(lowLimit, highLimit) {
  let result = 0
  const obj = {}
  
  for(let i=lowLimit; i<=highLimit; i++) {
    let tmp = 0
    const numString = String(i)
    
    for(j=0; j<numString.length; j++) {
      tmp += Number(numString[j])
    }
    
    if(obj[String(tmp)]) obj[String(tmp)]++
    else obj[String(tmp)] = 1
    
    result = Math.max(obj[String(tmp)], result)
  }
  
  return result
};
