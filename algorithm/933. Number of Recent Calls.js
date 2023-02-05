// 933. Number of Recent Calls
// src: https://leetcode.com/problems/number-of-recent-calls/description/

class RecentCounter {
  callStack:number[] = [];
  constructor() {
  
  }
  
  ping(t: number): number {
    this.callStack = this.callStack.filter((num) => t - num <= 3000)
    this.callStack.push(t)
    
    return this.callStack.length === 0 ? null : this.callStack.length
  }
}
