# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = {val: i for i, val in enumerate(inorder)}

        def helper(pre_idx, left, right):
            if left > right:
                return None
         
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            mid = in_map[root_val]

            root.left = helper(pre_idx + 1, left, mid - 1)

            root.right = helper(pre_idx + (mid - left) + 1, mid + 1, right)

            return root
      
        return helper(0, 0, len(inorder) - 1)
