// 16928
// https://www.acmicpc.net/problem/16928


package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
)


func main() {
	defer writer.Flush()
	var n, m int
	ladderMap := make(map[uint8]uint8)
	snakeMap := make(map[uint8]uint8)

	fmt.Fscanf(reader, "%d %d\n", &n, &m)

	for n > 0 || m > 0 {
		var s, d uint8
		fmt.Fscanf(reader, "%d %d\n", &s, &d)

		if n > 0 {
			ladderMap[s] = d
			n--
		} else {
			snakeMap[s] = d
			m--
		}
	}

	queue := make([][]uint8, 0)
	queue = append(queue, []uint8{1, 1})
	visit := make([]bool, 101)
	visit[1] = true
	for len(queue) > 0 {
		now := queue[0][0]
		cnt := queue[0][1]

		queue = queue[1:]
		var idx uint8 = 6

		for idx > 0 {
			nxt := now + idx

			if nxt >= 100 {
				fmt.Println(cnt)
				return
			}

			if nxt <= 100 && !visit[nxt] {
				if ladderMap[nxt] > 0 {
					nxt = ladderMap[nxt]
				}
				if snakeMap[nxt] > 0{
					nxt = snakeMap[nxt]
				}

				if !visit[nxt] {
					queue = append(queue, []uint8{nxt, cnt + 1})
					visit[nxt] = true
				}
			}

			idx--
		}
	}
}