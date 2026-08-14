# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        if not root:
            return res
        # bfs approach using a q
        q = deque([root])

        while q:
            snapshot = len(q)
            res.append([])
            for _ in range(snapshot):
                curr = q.popleft()
                res[-1].append(curr.val)
                
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
        
        return res

        