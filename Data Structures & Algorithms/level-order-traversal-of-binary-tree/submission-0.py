# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        
        stk = [root]
        result = []

        while stk:
            vals = []
            nextLevel = []
            for n in stk:
                vals.append(n.val)
                if n.left: nextLevel.append(n.left)
                if n.right: nextLevel.append(n.right)
            stk = nextLevel
            result.append(vals)
        
        return result
            
                
