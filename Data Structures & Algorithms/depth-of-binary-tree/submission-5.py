# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # q bfs
        if not root:
            return 0
        q = deque([root])

        res = 0
        while q:
            # snap shot level
            level_len = len(q)
            res += 1
            for _ in range(level_len):
                curr = q.popleft()
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)

        return res