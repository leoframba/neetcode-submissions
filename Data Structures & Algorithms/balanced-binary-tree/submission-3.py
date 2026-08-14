# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        valid = True
        def dfs(node) -> int:
            nonlocal valid
            # wall
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            delta = abs(right - left)
            if delta > 1:
                valid = False
            return max(left, right) + 1
            

        dfs(root)
        return valid
        