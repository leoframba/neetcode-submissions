# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre order gives us the root at pre[0]

        # in order tells us that all nodes left of the root are on the left and those right are on the right

        # key is the node val -> inorder index
        order_map = {val : i for i, val in enumerate(inorder)}

        
        p_idx = 0
        # we use a left and a right to track our location in the inorder array
        def to_tree(left, right):
            nonlocal p_idx
            #wall
            if left > right:
                return

            node = TreeNode(preorder[p_idx])
            in_idx = order_map[node.val]    

            p_idx += 1

            node.left = to_tree(left, in_idx - 1)
            node.right = to_tree(in_idx + 1, right)
           
            return node
        
        return to_tree(0, len(preorder) - 1)
        