// 1154. Day of the Year
// src: https://leetcode.com/problems/day-of-the-year/description/

var dayOfYear = function(date) {
  const standard = new Date(`${date.slice(0,4)}-01-01`)
  const now = new Date(date).getTime()
  
  return (now - standard) / 86400000 + 1
};
