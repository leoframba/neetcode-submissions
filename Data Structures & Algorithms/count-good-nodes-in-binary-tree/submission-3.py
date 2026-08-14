# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        stk = [(root, root.val)]
        result = 0

        while stk:
            cur, path_max = stk.pop()
            if cur.val >= path_max:
                result += 1
            
            new_max = max(path_max, cur.val)
            if cur.right: stk.append((cur.right, new_max))
            if cur.left: stk.append((cur.left, new_max))

        
        return result
