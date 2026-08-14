# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # we are going to travel over every node and check weather we can complete left -> parent -> right

        res = float('-inf')
        def max_path(node) -> int:
            if not node:
                return 0
            nonlocal res

            left = max(max_path(node.left), 0)
            right = max(max_path(node.right), 0)

            # we can take the path from the left right or the combine
            combine = left + right + node.val
                
            res = max(res, combine)
            return node.val + max(left, right)
        
        max_path(root)
        return res 
        