package main

// https://leetcode.com/problems/n-th-tribonacci-number/
func tribonacci(n int) int {
	vals := []int{0, 1, 1}
	if n <= 2 {
		return vals[n]
	}
	for i := 2; i < n; i++ {
		vals = append(vals, vals[i-2]+vals[i-1]+vals[i])
	}
	return vals[n]
}
