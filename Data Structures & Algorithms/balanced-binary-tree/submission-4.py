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
        
        def dfs(node) -> int:
            # wall
            if not node:
                return 0
            
            left = dfs(node.left)
            if left == -1:
                return -1
            right = dfs(node.right)
            if right == -1:
                return -1
            

            delta = abs(right - left)
            if delta > 1:
                return - 1
            return max(left, right) + 1
            
        res = dfs(root)
        return False if res == -1 else True
        