class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # down or right
        # Unique paths - bfs/dfs
        # track # of paths using recursion

        # edge case - no graph
        if m == 0 or n == 0: 
            return 0
        
        # at each state - how many paths can reach it
        # Paths that can reach the current state = left + up

        # define a grid + base case
        row, col = m, n

        grid = [
            [0 for _ in range(col + 1)] 
            for _ in range(row + 1)
        ]

        # we are running it backwards and starting from the base case
        # base case is 1 as its target
        grid[1][1] = 1
        
        # we start from the base case
        for r in range(1, row + 1):
            for c in range(1, col + 1):
                # state = 
                left = grid[r][c - 1]
                up = grid[r - 1][c]
                grid[r][c] += left + up
        
        return grid[m][n]
                


        
        