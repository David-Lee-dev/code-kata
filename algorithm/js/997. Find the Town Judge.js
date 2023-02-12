// 997. Find the Town Judge
// https://leetcode.com/problems/find-the-town-judge/description/

/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
  const result = new Array(n + 1)
  
  for(let t of trust) {
    result[t[0]] = -n
    
    if(result[t[1]]) result[t[1]]++
    else result[t[1]] = 1
  }
  console.log(result)
  for(let i=1; i<result.length; i++) {
    if(!result[i]) result[i] = 0
    if(result[i] === n - 1) return i
  }
  
  return -1
};
