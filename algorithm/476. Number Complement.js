// 476. Number Complement
// https://leetcode.com/problems/number-complement/description/

var findComplement = function(num) {
  let result = 0
  
  let i = 0;
  while(num > 1) {
    result += Math.pow(2, i) * (num % 2 === 0 ? 1 : 0)
    num = Math.floor(num / 2)
    i++;
  }
  
  return result + (Math.pow(2, i) * (num === 0 ? 1 : 0))
};
