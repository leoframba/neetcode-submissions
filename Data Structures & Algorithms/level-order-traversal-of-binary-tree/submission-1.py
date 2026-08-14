# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []
        
        def helper(level: List[TreeNode]):
            children = []
            vals = []
            for n in level:
                vals.append(n.val)
                if n.left: children.append(n.left)
                if n.right: children.append(n.right)
            self.result.append(vals)
            if children: helper(children)
        
        if root: helper([root])
        return self.result
        # if not root: return []

        
        # stk = [root]
        # result = []

        # while stk:
        #     vals = []
        #     nextLevel = []
        #     for n in stk:
        #         vals.append(n.val)
        #         if n.left: nextLevel.append(n.left)
        #         if n.right: nextLevel.append(n.right)
        #     stk = nextLevel
        #     result.append(vals)
        
        # return result
            
                
