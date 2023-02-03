// 13. Roman to Integer
// src: https://leetcode.com/problems/roman-to-integer/description/

var romanToInt = function(s) {
  const TABLE = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
  }
  
  var num = TABLE[s[0]];
  var result = 0;
  for(let idx = 1; idx < s.length; idx++) {
    var now = s[idx]
    var prev = s[idx - 1]
    
    if (num === 0){
      num = TABLE[now]
      continue
    }
    
    if (TABLE[now] < TABLE[prev]){
      result += num
      num = TABLE[now]
    }
    else if(TABLE[now] === TABLE[prev])  {
      num += TABLE[now];
    }
    else {
      num = TABLE[now] - num
    }
    
  }
  return result + num
};
