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

        # rather than keeping track of the entire grid - we can keep track of two rows
        # current row for the left val and r - 1 for the up val
        # grid = [
        #     [0 for _ in range(col + 1)] 
        #     for _ in range(row + 1)
        # ]
        prev = [0 for _ in range(col + 1)] # The first prev is all 0s as its an invalid path
        curr = [0 for _ in range(col + 1)]
        curr[1] = 1 # base case = entrance path 

        # we are running it backwards and starting from the base case
        # base case is 1 as its target
        # grid[1][1] = 1
        
        # calc for each row
        for r in range(row):
            for c in range(1, col + 1): # we pad the cols for left + base
                curr[c] += curr[c - 1] + prev[c]
            prev = curr # iterate rows
            curr = [0 for _ in range(col + 1)]
        
        return prev[col]
                


        
        