from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # edge case - empty input = 0 islands
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        # Assuming read only data we'll keep a visited grid - we could also just create a copy of the grid and modify that
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        # iterative bfs approach
        def bfs(start_state):
            q = deque([start_state])

            while q:
                r, c = q.popleft()

                # base - out ouf bounds - if not in bounds
                if not (0 <= r < rows and 0 <= c < cols):
                    continue
                # we use a visited list instead of tracking land/water
                # base - we only visite each grid space once
                if visited[r][c]:
                    continue
                
                # set visited
                visited[r][c] = True

                # Add all neighbors to the q
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    # Going to prune out of bounds/visited here aswell to prevent extra looping - we could remove the loop base cases
                    # we only proccess nodes that are islands
                    # an island must be inbound
                    is_inbounds_and_land = (0 <= nr < rows and 0 <= nc < cols) and grid[r][c] == '1'
                    if is_inbounds_and_land:
                        q.append((nr, nc))
            return
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    res += 1
                    bfs((r, c))  
        
        return res
                
