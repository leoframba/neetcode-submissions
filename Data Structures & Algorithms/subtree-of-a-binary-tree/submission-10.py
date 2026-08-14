# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def same(n1, n2) -> bool:
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False

            # if we find matching roots we look for the rest of the subtree
            return n1.val == n2.val and same(n1.left, n2.left) and same(n1.right, n2.right)
        
        def travel(r1, r2):
            if not r2:
                return True
            if not r1:
                return False
            
            return same(r1, r2) or travel(r1.left, r2) or travel(r1.right, r2)

        return travel(root, subRoot)


        