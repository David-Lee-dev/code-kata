// 11726
// https://www.acmicpc.net/problem/11726

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
	var n int
	
	fmt.Fscanf(reader, "%d\n", &n)

	if(n < 2) {
		fmt.Println(1)
		return
	}

	dp := make([]int, n)
	dp[0] = 1
	dp[1] = 2
	for i := 2; i < n; i++ {
		dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
	}

	fmt.Println(dp[n - 1])
}