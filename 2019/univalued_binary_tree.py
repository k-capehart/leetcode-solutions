# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def dfs(node, val, res):
            if node.val != val:
                return False
            if node.left != None:
                res = dfs(node.left, val, res)
            if node.right != None:
                res = dfs(node.right, val, res)
            return res
        return dfs(root, root.val, True)