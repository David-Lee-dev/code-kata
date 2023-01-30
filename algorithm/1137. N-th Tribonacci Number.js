// 1137. N-th Tribonacci Number
// src: https://leetcode.com/problems/n-th-tribonacci-number/description/

var tribonacci = function(n) {
  dp = [0, 1, 1]
  
  for(let i = 3; i <= n; i++) {
    dp.push(dp[i-3] + dp[i-2] + dp[i-1])
  }
  
  if (n < 3) return dp[n]
  
  return dp.pop()
};
