# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True

        def getHeight(node: TreeNode) -> int:
            if not node:
                return 0

            left_h = getHeight(node.left)
            right_h = getHeight(node.right)

            if abs(left_h - right_h) > 1:
                self.bal = False

            return 1 + max(right_h, left_h)

        getHeight(root)
        return self.bal