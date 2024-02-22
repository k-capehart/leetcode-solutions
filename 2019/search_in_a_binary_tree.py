# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root.val == val:
            return root
        if root.left != None and val < root.val:
            return self.searchBST(root.left, val)
        if root.right != None and val > root.val:
            return self.searchBST(root.right, val)
        return None