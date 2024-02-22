# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None: return False
        return self.traverseTree(root, root.val, sum)
        
    def traverseTree(self, node, val, sum):
        path_found = False
        
        if(val == sum and node.left == None and node.right == None):
            path_found = True
        
        if path_found == False and node.left != None:
            path_found = self.traverseTree(node.left, val + node.left.val, sum)
        if path_found == False and node.right != None:
            path_found = self.traverseTree(node.right, val + node.right.val, sum)
        
        return path_found