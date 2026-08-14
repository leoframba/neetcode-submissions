# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # We need to find the number of values in the the tree
        # because its a bst we could always convert it to a list and do -index to find the val but would require more mem

        # DFS with a count

        count = 0
        res = None
        def dfs(node):
            nonlocal res, count
            if not node:
                return
            
            
            # go all the way left
            left = dfs(node.left)
            # We are at k = 1
            count += 1
            if count == k:
                res = node.val
            
            # look right
            right = dfs(node.right)

            return 
        
        dfs(root)
        return res
            

                
        