from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        return self.flipLinks(None, head)

    def flipLinks(self, prev_node: Optional[ListNode], node: Optional[ListNode]) -> Optional[ListNode]:
        if not node.next:
            node.next = prev_node
            return node
        next_node = self.flipLinks(node, node.next)
        node.next = prev_node
        return next_node
