# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []

        cur = root

        while stk or cur:
            
            while cur:
                stk.append(cur)
                cur = cur.left
        
            cur = stk.pop()
            k = k - 1

            if k == 0:
                return cur.val

            cur = cur.right

        
        return -1