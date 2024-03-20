package main

import "math"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
func maxLevelSum(root *TreeNode) int {
	if root == nil {
		return 0
	}

	queue := []*TreeNode{root}
	max := math.MinInt
	var level, maxLevel int

	for len(queue) > 0 {
		levelLen := len(queue)
		level++
		sum := 0
		for i := 0; i < levelLen; i++ {
			root = queue[i]
			sum = sum + root.Val
			if root.Left != nil {
				queue = append(queue, root.Left)
			}
			if root.Right != nil {
				queue = append(queue, root.Right)
			}
		}
		if sum > max {
			max = sum
			maxLevel = level
		}
		queue = queue[levelLen:]
	}
	return maxLevel
}
