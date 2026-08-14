# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs approach

        res = 0
        def dfs(node) -> (int, int):  
            #wall
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            depth = max(left[0] + 1, right[0] + 1)
            di = max(left[0] + right[0], right[1], left[1])
            return (depth, di)
            
        res = dfs(root)
        res = max(res[0] - 1, res[1])
        return res
        