package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// https://leetcode.com/problems/binary-tree-right-side-view/
func rightSideView(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	queue := []*TreeNode{root}
	rightSideValues := []int{}
	for len(queue) > 0 {
		levelLen := len(queue)
		for i := 0; i < levelLen; i++ {
			root = queue[i]
			if root.Left != nil {
				queue = append(queue, root.Left)
			}
			if root.Right != nil {
				queue = append(queue, root.Right)
			}
		}
		queue = queue[levelLen:]
		rightSideValues = append(rightSideValues, root.Val)
	}
	return rightSideValues
}
