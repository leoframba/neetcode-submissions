# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize with a very small number
        self.max_sum = float('-inf')

        def get_gain(node):
            if not node:
                return 0
            
            # 1. Recursively get the max gain from subtrees
            # If a gain is negative, we take 0 (ignore that path)
            left_gain = max(get_gain(node.left), 0)
            right_gain = max(get_gain(node.right), 0)
            
            # 2. Check if the path passing THROUGH this node is the global max
            # This is the "arc" path: left -> node -> right
            current_path_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # 3. Return the best "single-leg" path to the parent
            # The parent can only pick ONE branch to continue the path
            return node.val + max(left_gain, right_gain)

        get_gain(root)
        return self.max_sum   