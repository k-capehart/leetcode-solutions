package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// https://leetcode.com/problems/search-in-a-binary-search-tree/
func searchBST(root *TreeNode, val int) *TreeNode {
	if root == nil || root.Val == val {
		return root
	}

	if val > root.Val {
		return searchBST(root.Right, val)
	}
	return searchBST(root.Left, val)
}
