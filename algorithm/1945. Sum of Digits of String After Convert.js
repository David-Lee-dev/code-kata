// 1945. Sum of Digits of String After Convert
// src: https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

var getLucky = function(s, k) {
  let stringToNumber = s.split('').map(alpha => String(alpha.charCodeAt(0) - 96)).join('')
  const transform = (string) => String(string.split('').reduce((acc, cur) => acc + Number(cur), 0))
  
  while(k > 0) {
    stringToNumber = transform(stringToNumber)
    k--
  }
  
  return Number(stringToNumber)
};
