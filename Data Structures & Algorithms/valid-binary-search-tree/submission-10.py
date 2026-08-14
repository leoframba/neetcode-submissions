# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BST - DFS search need to make sure nodes are within a set range

        # track two vals - min/mx
        # min/max depend on left/right
        def dfs(node, low, high) -> bool:
            # wall
            if not node:
                return True
            
            #is the current node within range?
            if node.val >= high or node.val <= low:
                return False
            
            left = dfs(node.left, low, node.val)
            right = dfs(node.right, node.val, high)

            return left and right

        return dfs(root, float('-inf'), float('inf'))


        