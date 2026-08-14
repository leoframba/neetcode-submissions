# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stk = [(root, float('-inf'), float('inf'))]
       
        while stk:
            cur, low, high = stk.pop()
            if not (low < cur.val < high):
                return False

            if cur.right: stk.append((cur.right, cur.val, high))            
            if cur.left: stk.append((cur.left, low, cur.val))
        
        return True

        # def helper(node, low, high)-> bool:
        #     if not node: return True

        #     if not (low < node.val < high):
        #         return False
            
        #     return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        
        # return helper(root, float('-inf'), float('inf'))