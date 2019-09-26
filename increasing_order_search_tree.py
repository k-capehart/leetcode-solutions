# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:   
        res = []
        def dfs(root):
            if root.left == None and root.right == None:
                res.append(root.val)
                return
            if root.left != None:
                dfs(root.left)
            res.append(root.val)
            if root.right != None:
                dfs(root.right)
            return
        dfs(root)
        tree_node = TreeNode(res[0])
        temp_node = tree_node
        for i in range(len(res)-1):
            temp_node.left = None
            temp_node.right = TreeNode(res[i+1])
            temp_node = temp_node.right
        return tree_node