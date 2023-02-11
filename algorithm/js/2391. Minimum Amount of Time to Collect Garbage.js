// 2391. Minimum Amount of Time to Collect Garbage
// https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description/

/**
 * @param {string[]} garbage
 * @param {number[]} travel
 * @return {number}
 */
const METAL = 0
const PAPER = 1
const GLASS = 2

const SPANED_TIME = 0
const TRAVEL_TIME = 1

var garbageCollection = function(garbage, travel) {
  const timeOfTruck = [[0, 0], [0, 0], [0, 0]]
  travel = [0, ...travel]
  
  var seperateCollection = function (garbages) {
    const garbageCnt = [0, 0, 0]
    
    for(let i=0; i<garbages.length; i++) {
      if(garbages[i] === 'M') garbageCnt[METAL]++
      if(garbages[i] === 'P') garbageCnt[PAPER]++
      if(garbages[i] === 'G') garbageCnt[GLASS]++
    }
    
    return garbageCnt
  }
  
  for(let house=0; house<garbage.length; house++) {
    const collectTime = seperateCollection(garbage[house])
    
    for(let type=0; type<3; type++) {
      if(collectTime[type] > 0) {
        timeOfTruck[type][SPANED_TIME] += timeOfTruck[type][TRAVEL_TIME] + collectTime[type] + travel[house]
        timeOfTruck[type][TRAVEL_TIME] = 0
      } else {
        timeOfTruck[type][TRAVEL_TIME] += travel[house]
      }
    }
  }
  
  return timeOfTruck[METAL][SPANED_TIME] + timeOfTruck[PAPER][SPANED_TIME] + timeOfTruck[GLASS][SPANED_TIME]
};
