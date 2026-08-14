"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # connected -> all nodes are reachable
        # undirected -> edges dont have directions

        # edge case - empty input
        if not node:
            return None
        
        #approach use a map to map og node -> copy

        copy_map = {}

        # iterative approach/dfs
        stack = [node]

        # create all nodes
        while stack:
            curr = stack.pop()

            if curr in copy_map:
                continue
            
            # create copy + link
            cpy = Node(curr.val)
            copy_map[curr] = cpy

            # append all neighbors that havent been copied
            for n in curr.neighbors:
                if n not in copy_map:
                    stack.append(n)
        
        # link 
        stack.append(node)
        visited = {node.val} 
        while stack:
            curr = stack.pop()
            curr_cpy = copy_map[curr]
            
            for n in curr.neighbors:
                if n.val not in visited:
                    stack.append(n)
                    visited.add(n.val)
                curr_cpy.neighbors.append(copy_map[n])
        
        return copy_map[node]



        
