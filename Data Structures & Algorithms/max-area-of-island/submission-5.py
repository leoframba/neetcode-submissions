class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        self.max_size = 0
        self.cur_size = 0

        def dfs(self, r, c):
            #bounds check
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return
            
            # mark visited
            grid[r][c] = -1
            
            #increase size and check vs max
            self.cur_size += 1

            #look all directions
            dfs(self, r - 1, c)
            dfs(self, r + 1, c)
            dfs(self, r, c - 1)
            dfs(self, r, c + 1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    #calc island
                    dfs(self, r, c)
                    self.max_size = max(self.max_size, self.cur_size)
                    self.cur_size = 0
        
        return self.max_size
        