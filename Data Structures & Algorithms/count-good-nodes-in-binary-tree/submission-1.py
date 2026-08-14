# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        stk = [(root, float('-inf'))]
        result = 0

        while stk:
            cur, path_max = stk.pop()
            if cur.val >= path_max:
                path_max = max(path_max, cur.val)
                result += 1
            if cur.left: stk.append((cur.left, path_max))
            if cur.right: stk.append((cur.right, path_max))
        
        return result