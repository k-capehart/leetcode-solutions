package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteMiddle(head *ListNode) *ListNode {
	if head.Next == nil {
		return nil
	}

	if head.Next.Next == nil {
		head.Next = nil
		return head
	}

	var node = head
	var nodes = []*ListNode{node}
	for node.Next != nil {
		node = node.Next
		nodes = append(nodes, node)
	}

	var middle = len(nodes) / 2

	nodes[middle-1].Next = nodes[middle+1]

	return head
}
