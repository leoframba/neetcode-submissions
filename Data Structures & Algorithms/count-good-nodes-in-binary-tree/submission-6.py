# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = [(root, float('-inf'))]
        res = 0
        while stack:
            node, m = stack.pop()

            if node.val >= m:
                res += 1
                m = node.val
            
            if node.left: stack.append((node.left, m))
            if node.right: stack.append((node.right, m))
        
        return res


        
        