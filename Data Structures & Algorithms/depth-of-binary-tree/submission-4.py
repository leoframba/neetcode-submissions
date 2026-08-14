# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        #stack approach
        if not root:
            return 0

        #bfs
        stack = [root]
        next = []
        res = 0
        while stack:
            next = stack.copy()
            stack.clear()
            res += 1
            while next:
                curr = next.pop()
                if curr.left:
                    stack.append(curr.left)
                if curr.right: 
                    stack.append(curr.right)
            
        return res
                



        