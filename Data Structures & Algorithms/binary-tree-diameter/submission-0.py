# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0

        def getHeight(node: TreeNode) -> int:
            # null/no node
            if not node:
                return 0

            # look r/lk recur
            left_h = getHeight(node.left)
            right_h = getHeight(node.right)

            # pot d is the left + right h
            self.max_d = max(self.max_d, left_h + right_h)

            # return height
            return 1 + max(left_h, right_h)
        
        getHeight(root)
        return self.max_d