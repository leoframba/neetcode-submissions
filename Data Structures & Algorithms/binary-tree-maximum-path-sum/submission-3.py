class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize our global max with negative infinity
        self.global_max = float('-inf')
        
        def get_max_branch(node: Optional[TreeNode]) -> int:
            # Base case: an empty node contributes 0 to the path
            if not node:
                return 0
            
            # 1. Recursively get the max branch sums from left and right children
            # If a branch is negative, we ignore it by taking max(..., 0)
            left_branch = max(get_max_branch(node.left), 0)
            right_branch = max(get_max_branch(node.right), 0)
            
            # 2. Calculate the max path sum IF this node is the highest point (the V-shape)
            current_path_sum = node.val + left_branch + right_branch
            
            # 3. Update the global maximum if this new path is better
            self.global_max = max(self.global_max, current_path_sum)
            
            # 4. Return the max straight-line branch up to the parent
            return node.val + max(left_branch, right_branch)
            
        # Kick off the recursion
        get_max_branch(root)
        
        return self.global_max