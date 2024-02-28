// 11723
// https://www.acmicpc.net/problem/11723


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

var (
	checker = make([]bool, 20)
)

func main() {
	defer writer.Flush()
	var M, num int
	var command string

	fmt.Fscanf(reader, "%d\n", &M)

	for M > 0 {
		fmt.Fscanf(reader, "%s %d\n", &command, &num)
		execute(command, num)
		M--
	}
}

func execute(c string, n int) {
	idx := n - 1
	if c == "add" {
		checker[idx] = true
	} else if c == "remove" {
		checker[idx] = false
	} else if c == "toggle" {
		checker[idx] = !checker[idx]
	} else if c == "all" {
		fillChecker(true)
	} else if c == "empty" {
		fillChecker(false)
	} else {
		printNum(checker[idx])
	}
}

func printNum(flag bool) {
	if(flag) {
		fmt.Fprintf(writer ,"%d\n", 1)
	} else {
		fmt.Fprintf(writer ,"%d\n", 0)
	}
}

func fillChecker(value bool) {
	for i := range checker {
		checker[i] = value
	}
}