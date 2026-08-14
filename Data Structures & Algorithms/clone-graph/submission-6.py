"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        # recursive approach

        cpy_map = {}
        def dfs(node: Optional['Node']) -> Optional['Node']:
            # base - already visited
            if node in cpy_map:
                return cpy_map[node]

            # else create
            cpy = Node(node.val)
            cpy_map[node] = cpy

            # link all neighbors
            for n in node.neighbors:
                cpy_n = dfs(n)
                cpy.neighbors.append(cpy_n)
            
            return cpy
        
        return dfs(node)
            
    

        