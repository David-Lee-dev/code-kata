// 11724
// https://www.acmicpc.net/problem/11724

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

type Graph struct {
	adjacencyMap map[int][]int
}

func NewGraph() *Graph {
	return &Graph{
		adjacencyMap: make(map[int][]int),
	}
}

func(g *Graph) InitGraph(n int) {
	for n > 0 {
		g.adjacencyMap[n] = make([]int, 0)
		n--
	}
}

func (g *Graph) AddEdge(src, dest int) {
	g.adjacencyMap[src] = append(g.adjacencyMap[src], dest)
	g.adjacencyMap[dest] = append(g.adjacencyMap[dest], src)
}

func DFS(g *Graph, vertex int, visit *[]bool) {
	visited :=*visit
	
	for _, n := range g.adjacencyMap[vertex] {
		if(!visited[n - 1]) {
			visited[n - 1] = true
			DFS(g, n, visit)
		}
	}
}

func isInArray(arr []int, target int) bool {
	for _, element := range arr {
			if element == target {
					return true
			}
	}
	return false
}

func main() {
	defer writer.Flush()
	
	var N, M int

	fmt.Fscanf(reader, "%d %d\n", &N, &M)

	graph := NewGraph()
	graph.InitGraph(N)
	visit := make([]bool, N)
	result := 0
	
	for M > 0 {
		var n1, n2 int
		fmt.Fscanf(reader, "%d %d\n", &n1, &n2)

		graph.AddEdge(n1, n2)
		M--
	}

	for vertex := range graph.adjacencyMap {
		if(!visit[vertex - 1]) {
			visit[vertex - 1] = true
			DFS(graph, vertex, &visit)
			result++
		}
	}

	fmt.Println(result)
}