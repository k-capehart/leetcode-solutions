package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func goodNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}

	sum := 1
	if root.Left != nil {
		sum = traverse(root.Left, root.Val) + sum
	}
	if root.Right != nil {
		sum = traverse(root.Right, root.Val) + sum
	}
	return sum
}

func traverse(root *TreeNode, maxVal int) int {
	sum := 0
	if root.Val >= maxVal {
		sum++
		maxVal = root.Val
	}

	if root.Left != nil {
		sum = traverse(root.Left, maxVal) + sum
	}
	if root.Right != nil {
		sum = traverse(root.Right, maxVal) + sum
	}
	return sum
}
