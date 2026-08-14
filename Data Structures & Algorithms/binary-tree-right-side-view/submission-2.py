# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # bfs but only append last item of every row. So we will build a row list and append -1
        # we have to proccess left to right
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            # proccess final item in the list
            res.append(q[-1].val)

            # add new items
            snapshot = len(q)
            for _ in range(snapshot):
                curr = q.popleft()
                # append left first to make sure right most val is last
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            
        return res
        
        