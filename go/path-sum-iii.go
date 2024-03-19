package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// https://leetcode.com/problems/path-sum-iii
func pathSum(root *TreeNode, targetSum int) int {
	if root == nil {
		return 0
	}

	return traversePathSum(root, targetSum, 0) + pathSum(root.Left, targetSum) + pathSum(root.Right, targetSum)
}

func traversePathSum(root *TreeNode, targetSum int, sum int) int {
	if root == nil {
		return 0
	}

	count := 0
	if root.Val+sum == targetSum {
		count++
	}

	lCount := traversePathSum(root.Left, targetSum, sum+root.Val)
	rCount := traversePathSum(root.Right, targetSum, sum+root.Val)

	return lCount + rCount + count
}
