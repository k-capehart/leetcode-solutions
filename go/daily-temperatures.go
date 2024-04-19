package main

// https://leetcode.com/problems/daily-temperatures/
func dailyTemperatures(temperatures []int) []int {
	var matrix [101][]int
	ans := make([]int, len(temperatures))
	for i, temp := range temperatures {
		matrix[temp] = append(matrix[temp], i)
		for j := 30; j < temp; j++ {
			if len(matrix[j]) > 0 {
				for x := 0; x < len(matrix[j]); x++ {
					ans[matrix[j][x]] = i - matrix[j][x]
				}
				matrix[j] = []int{}
			}
		}
	}
	return ans
}
