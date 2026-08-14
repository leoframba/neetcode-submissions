# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return None
        
        def containsAncestor(n: TreeNode, p: TreeNode, q: TreeNode):
            if not n: return False
            
            if not n or n.val == p.val or n.val == q.val:
                return True
            
            return containsAncestor(n.left, p, q) or containsAncestor(n.right, p, q)
        
        left = containsAncestor(root.left, p, q)
        right = containsAncestor(root.right, p, q)
        
        print(root.val)
        print(left)
        print(right)

        if root.val == p.val or root.val == q.val and (left or right):
            return root

        if left and right:
            return root
        
        if left:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)