from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque()

        # search the grid
        fresh_count = 0
        for r in range(rows):
            for c in range(cols):
                # if we find a rotten fruit get the cords
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        
        mins = 2
        # multi bfs
        while q:
            r, c = q.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                # bounds + fresh fruit
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    fresh_count -= 1
                    grid[nr][nc] = mins = grid[r][c] + 1
                    q.append((nr, nc))
        
        # # search the grid for fresh
        # for r in range(rows):
        #     for c in range(cols):
        #         # if we find a rotten fruit get the cords
        #         if grid[r][c] == 1:
        #             return -1
        print(fresh_count)
        return -1 if fresh_count > 0 else mins - 2
        

        




