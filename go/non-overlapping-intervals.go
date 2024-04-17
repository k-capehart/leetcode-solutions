package main

import (
	"cmp"
	"slices"
)

// https://leetcode.com/problems/non-overlapping-intervals/
func eraseOverlapIntervals(intervals [][]int) int {
	slices.SortFunc(intervals, func(a, b []int) int {
		return cmp.Compare(a[1], b[1])
	})

	count := 0
	for i := 1; i < len(intervals); i++ {
		if intervals[i][0] < intervals[i-1][1] {
			count++
			intervals[i][1] = intervals[i-1][1]
		}
	}

	return count
}
