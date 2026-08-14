# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # create a preorder string

        res = []

        def dfs(node):
            if not node:
                res.append('Null')
                return
            
            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

            return

        dfs(root)
        print(res)
        return ",".join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        preorder = data.split(',')

        i = 0
        def dfs():
            nonlocal i

            if preorder[i] == 'Null':
                i += 1
                return None
            
            #Create current node
            node = TreeNode(preorder[i])

            i += 1
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()



