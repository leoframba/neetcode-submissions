# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # dfs search to find path
        # maintain a running max

        res = 0
        def dfs(node, m):
            nonlocal res
            if not node:
                return 
            
            if node.val >= m:
                res += 1
                m = node.val
            
            dfs(node.left, m)
            dfs(node.right, m)
        
        dfs(root, root.val)
        return res
        
        

        