package main

import "math"

// https://leetcode.com/problems/cycle-length-queries-in-a-tree
func cycleLengthQueries(n int, queries [][]int) []int {
	var answers []int
	for _, query := range queries {
		a := query[0]
		b := query[1]
		x1 := int(math.Log2(float64(a)))
		x2 := int(math.Log2(float64(b)))

		count := int(math.Abs(float64(x2 - x1)))
		if a > b {
			a = int(a / int(math.Pow(2, float64(count))))
		} else {
			b = int(b / int(math.Pow(2, float64(count))))
		}

		for a != b {
			a = int(a / 2)
			b = int(b / 2)
			count += 2
		}
		answers = append(answers, count+1)
	}
	return answers
}
