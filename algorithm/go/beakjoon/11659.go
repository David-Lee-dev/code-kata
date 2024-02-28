// 11659
// https://www.acmicpc.net/problem/11659


package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	defer writer.Flush()

	var N, M int

	fmt.Fscanf(reader, "%d %d\n", &N, &M)
	sums := getSums(N)

	for i := 0; i < M; i++ {
		var s, e int
		fmt.Fscanf(reader, "%d %d\n", &s, &e)

		result := sums[e - 1]
		if(s > 1) {
			result -= sums[s - 2]
		}
		fmt.Fprintln(writer, result)
	}
}

func getSums(N int) []int {
	nums := make([]int, N)
	sums := make([]int, N)
	numStr, _ := reader.ReadString('\n')
	numStr = strings.TrimSuffix(numStr, "\n")
	strNums := strings.Split(numStr, " ")

	total := 0
	for i, s := range strNums {
		nums[i], _ = strconv.Atoi(s)
		total += nums[i]
		sums[i] = total
	}

	return sums
}