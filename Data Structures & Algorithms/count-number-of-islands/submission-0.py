class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            # mark visited
            grid[r][c] = -1

            #get neighbors
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            neighbors = []
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    neighbors.append((nr, nc))
            
            for nr, nc in neighbors:
                if grid[nr][nc] == '1':
                    dfs(nr, nc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        
        return res