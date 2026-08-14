class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        #name of the game = detect a cycle and make sure all nodes are connected

        # Build an adj list
        # create a dict with key = curr and value = all connected currs
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b) # will need to include logic to prvent ping ponging between two currs
            adj[b].append(a)



        # visisted list contains an element for each curr. 
        # Elements will have 3 values 0 = unvisited, 1 = visiting, 2 = visited
        visited = [0] * n

        # given a curr will detect a cycle based on a 3 color dfs
        def has_cycle(curr: int, prev: int) -> bool:
            state = visited[curr]
            if state == 1: # If we visit a curr in our rec stack we have found a cycle
                return True
            if state == 2: # If we hit a curr we've already visited we knows its cycle free and can skip
                return False
            
            # we hit a curr that is unvisited
            # set it too visiting
            visited[curr] = 1

            # look at its neighbors
            for n in adj[curr]:
                if n != prev and has_cycle(n, curr):
                    return True
            
            visited[curr] = 2
            return False
        
        def count_connections(curr, prev) -> int:
            count = 1

            # look at its neighbors
            for n in adj[curr]:
                if n != prev:
                    count += count_connections(n, curr)
            
            return count

                    
        
        for i in range(n):
            if visited[i] == 0: # we only visit currs we havent already
                if has_cycle(i, -1):
                    return False

        print(count_connections(0, -1))
        return count_connections(0, -1) == n

        