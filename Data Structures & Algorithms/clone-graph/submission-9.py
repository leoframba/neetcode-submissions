"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # edge
        if not node:
            return None
        
        q = deque([node])
        cpy_map = {node: Node(node.val)}

        while q:
            curr = q.popleft()
            cpy = cpy_map.setdefault(curr, Node(curr.val))

            for n in curr.neighbors:
                if n not in cpy_map:
                    q.append(n)
                n_cpy = cpy_map.setdefault(n, Node(n.val))
                cpy.neighbors.append(n_cpy)
        
        return cpy_map[node]

            
        

        