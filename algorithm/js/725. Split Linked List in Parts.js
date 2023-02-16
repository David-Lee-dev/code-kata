// 725. Split Linked List in Parts
// https://leetcode.com/problems/split-linked-list-in-parts/description/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode[]}
 */
var splitListToParts = function(head, k) {
    var len = 0
    
    var trip = function(node) {
        if(node === null) return
        len++
        if(node.next) trip(node.next)
    }
    trip(head)

    const share = Math.floor(len / k)
    let reminder = len % k

    const indexes = []

    let start = 0
    let end = 0
    for(let i=0; i<k; i++) {
        const flag = (reminder > 0 ? 1 : 0)
        end = start + share + flag
        indexes.push(start === end ? null : end)

        start = end
        reminder--
    }

    const result = []
    var sol = function(node, head, cnt) {
        if(cnt > len || node === null) return

        if(cnt === indexes[0]) {
            tmp = node.next
            result.push(head)
            node.next = null
            indexes.shift()
            sol(tmp, tmp, cnt + 1)
        } else if (node === null){
            result.push(null)
            sol(null, null, cnt + 1)
        } else {
            sol(node.next, head, cnt + 1)
        }
    }
    sol(head, head, 1)

    for(let i=0; i<k-len; i++){
        result.push(null)
    }

    return result
};