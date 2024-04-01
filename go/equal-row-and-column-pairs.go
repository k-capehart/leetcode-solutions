package main

// https://leetcode.com/problems/equal-row-and-column-pairs/
func equalPairs(grid [][]int) int {
	if grid == nil {
		return 0
	}

	if len(grid) == 1 {
		return 1
	}

	rowMap := map[[200]int]int{}
	colMap := map[[200]int]int{}

	for i := 0; i < len(grid); i++ {
		col := [200]int{}
		row := [200]int{}
		for j := 0; j < len(grid); j++ {
			row[j] = grid[i][j]
			col[j] = grid[j][i]
		}
		rowMap[row]++
		colMap[col]++
	}
	count := 0
	for key, val := range rowMap {
		count = count + (val * colMap[key])
	}

	return count
}
