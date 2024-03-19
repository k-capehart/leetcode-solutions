package main

import "reflect"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// https://leetcode.com/problems/leaf-similar-trees/
func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	return reflect.DeepEqual(buildLeafValSeq(root2), buildLeafValSeq(root1))
}

func buildLeafValSeq(root *TreeNode) []int {
	if root == nil {
		return nil
	}

	if root.Left == nil && root.Right == nil {
		return []int{root.Val}
	}

	left := buildLeafValSeq(root.Left)
	right := buildLeafValSeq(root.Right)

	return append(left, right...)
}
