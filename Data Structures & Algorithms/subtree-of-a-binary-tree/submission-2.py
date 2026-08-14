# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if not subRoot: return False
        if not root: return False
        

        def isSameTree(n1: TreeNode, n2: TreeNode) -> bool:
            if not n1 and not n2:
                return True
            
            # not equal case
            if not n1 or not n2 or n1.val != n2.val:
                return False
            else:
                return isSameTree(n1.left, n2.left) and isSameTree(n1.right, n2.right)

        
        # if we have a matching root we check the rest of the tree
        if isSameTree(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)