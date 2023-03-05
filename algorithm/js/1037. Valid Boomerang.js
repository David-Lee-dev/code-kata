// 1037. Valid Boomerang
// https://leetcode.com/problems/valid-boomerang/description/

/**
 * @param {number[][]} points
 * @return {boolean}
 */
var isBoomerang = function(points) {
    points.sort((a, b) => a[0] - b[0])

    var firstX = (points[1][0] - points[0][0])
    var firstY = (points[1][1] - points[0][1])
    var secondX = (points[2][0] - points[1][0])
    var secondY = (points[2][1] - points[1][1])

    if ((firstX === 0 && firstY === 0) || (secondX === 0 && secondY === 0)) return false
    if (firstX / firstY === secondX / secondY) return false

    return true
};