package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// https://leetcode.com/problems/linked-list-cycle/
func hasCycle(head *ListNode) bool {
	if head == nil || head.Next == nil || head.Next.Next == nil {
		return false
	}

	slow := head
	fast := head.Next.Next

	for fast.Next != nil && fast.Next.Next != nil {
		if slow == fast {
			return true
		}
		slow = slow.Next
		fast = fast.Next.Next
	}

	return false
}
