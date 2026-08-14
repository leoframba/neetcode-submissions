class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if r >= rows or r < 0 or c < 0 or c >= cols or grid[r][c] != '1':
                return

            # mark visited
            grid[r][c] = '0'

            # check neighbors
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        
        return res