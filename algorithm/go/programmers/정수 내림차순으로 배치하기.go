// 정수 내림차순으로 배치하기
// https://school.programmers.co.kr/learn/courses/30/lessons/12933?language=go


import (
	"sort"
	"math"
)

type myArr []int64

func (a myArr) Len() int           { return len(a) }
func (a myArr) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a myArr) Less(i, j int) bool { return a[i] < a[j] }

func powInt64(x, y int64) int64 {
	return int64(math.Pow(float64(x), float64(y)))
}

func solution(n int64) int64 {
	arr := make(myArr, 0)
	
	for n > 0 {
			arr = append(arr, n % 10)
			n /= 10
	}

	sort.Sort(arr)
	
	var result int64 = 0
	for index, value := range arr {
			result += value * (powInt64(int64(10), int64(index)))
	}
	

	return result
}