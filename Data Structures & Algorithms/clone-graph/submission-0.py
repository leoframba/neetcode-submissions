"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # empty check
        if not node:
            return node
        
        visited: Dict[Node: Node] = {}

        visited[node] = Node(node.val, [])
        q = deque([node]) # use a q to track the nodes we have linked

        while q:
            curr = q.popleft()

            # if we havent seen this node make a copy
            if curr not in visited:
                visited[curr] = Node(curr.val, [])
            
            for n in curr.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val, [])
                    q.append(n)
                visited[curr].neighbors.append(visited[n])
        
        return visited[node]
        