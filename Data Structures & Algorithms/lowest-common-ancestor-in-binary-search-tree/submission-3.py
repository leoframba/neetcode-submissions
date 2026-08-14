# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # bst all left children are < parent all right >
        # common ancestor - both values inclduing oneself as a parent

        #? given a node how do we know its ancestors
        # Whats the smallest subset that contains both values - root of that subset is the awnser

        # find the split point
        def dfs(node):
            if not node:
                return None
            # 3 diferent snarios
            # both values are less than node
            if p.val < node.val and q.val < node.val:
                return dfs(node.left)
            #both are greater    
            elif p.val > node.val and q.val > node.val:
                return dfs(node.right)
            else:
                #split we found our node
                return node



        return dfs(root)
                
             

            


            
            

            





        