# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        def isSameNode(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1:
                if node2:
                    return False
                else:
                    return True
            else:
                if not node2:
                    return False
            
            if node1.val == node2.val:
                return isSameNode(node1.left, node2.left) and isSameNode(node1.right, node2.right)
            else:
                return False
        
        return isSameNode(p, q)