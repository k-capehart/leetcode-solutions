# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node, sum):
            if node.val >= L and node.val <= R:
                sum+=node.val
            if node.left == None and node.right == None:
                return sum
            
            if node.left != None:
                if node.left.val >= L:
                    sum = dfs(node.left, sum)
                elif node.left.right != None: 
                    sum = dfs(node.left.right, sum)
            if node.right != None:
                if node.right.val <= R:
                    sum = dfs(node.right, sum)
                elif node.right.left != None:
                    sum = dfs(node.right.left, sum)
            return sum
    
        return dfs(root, 0)