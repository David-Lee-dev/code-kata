// 2304. Minimum Path Cost in a Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-grid/description/

var minPathCost = function(grid, moveCost) {
  var ROW = grid.length
  var COL = grid[0].length
  var result = [grid[0]]
  
  for(let r=1; r<ROW; r++) {
    const tmpRow = []
    for(let outCol=0; outCol<COL; outCol++) {
      const buffer = []
      
      for (let inCol=0; inCol<COL; inCol++) {
        buffer.push(grid[r][outCol] + result[r-1][inCol] + moveCost[grid[r-1][inCol]][outCol])
      }
      tmpRow.push(Math.min(...buffer))
    }
    result.push(tmpRow)
  }
  return Math.min(...result[result.length-1])
};
