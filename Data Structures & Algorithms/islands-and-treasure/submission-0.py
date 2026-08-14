class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
            rows, cols = len(grid), len(grid[0])


            def dfs(r, c, d):

                # bounds check + check that we arent on another chest/water
                if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] < d:
                    return

                # if we are here we have found a land
                grid[r][c] = d

                # look at neighbors
                dfs(r - 1, c, d + 1)
                dfs(r + 1, c, d + 1)
                dfs(r, c - 1, d + 1)
                dfs(r, c + 1, d + 1)



            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 0:
                        dfs(r, c, 0)
        