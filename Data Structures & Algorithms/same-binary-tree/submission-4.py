# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
        #     return True
        
        # if not p or not q or p.val != q.val:
        #     return False
                
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        qu = deque([(p, q)])

        while qu:
            n1, n2 = qu.popleft()
            if not n1 and not n2: continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
            qu.append((n1.left, n2.left))
            qu.append((n1.right, n2.right))
        return True