class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # we need to visit all nodes to view connections
        # Im going to use this set to keep track of nodes that ive already visited
        visited = set()

        # create an adj list for dfs search
        adj = {i: [] for i in range(n)} # For each node well have a list of its neighbors
        for a, b in edges:
            adj[a].append(b) # we appened edges both ways because our graph is UNdirected
            adj[b].append(a)



        def dfs(curr, prev):
            if curr in visited:
                return # redundent?
            visited.add(curr)

            for neighbor in adj[curr]:
                if neighbor != prev and neighbor not in visited: # prevent ping pong
                    dfs(neighbor, curr)
            return

        res = 0

        # im going to iterate through every node to look for connections. I will skip a node if ive already visited it via a prior nodes connection
        for node in range(n):
            if node not in visited:
                dfs(node, -1)
                res += 1
        
        return res



        