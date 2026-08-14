class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # edge case - empty input = 0 islands
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        # sink all adj
        def bfs(r: int, c: int):
            # base - invalid cords ie out of bounds
            if not (0 <= r < rows and 0 <= c < cols):
                return
            # base - already water ie invalid island tile
            if grid[r][c] == '0':
                return
            
            # sink current island so we dont count it twice
            grid[r][c] = '0'

            # search
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                bfs(r + dr, c + dc)

            return 
        
        # Plan of attack - Iterate over the graph and preform bfs
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res += 1 #found an island
                    bfs(r, c) #sink it
        
        return res
        