//22. Generate Parentheses
//https://leetcode.com/problems/generate-parentheses/
/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    var result = []
    var sol = function(left, right, string) {
        if(left === 0 && right === 0) {
            result.push(string)
            return
        }
        //open
        if(left > 0) sol(left - 1, right, string + '(')
        //close
        if(left < right && right > 0) sol(left, right - 1, string + ')')
    }
    sol(n, n, '')

    return result
};