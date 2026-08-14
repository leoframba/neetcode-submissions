from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # Union Find Setup
        parents = [i for i in range(rows * cols)]

        def find(i):
            if parents[i] == i:
                return i
            parents[i] = find(parents[i])
            return parents[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parents[root_i] = root_j
                return True
            return False

        # Flatten and sort by elevation (which equals time)
        flattened = [
            (val, r, c) 
            for r, row in enumerate(grid) 
            for c, val in enumerate(row)
        ]
        flattened.sort()

        start_node = 0                     # Top-Left: (0, 0)
        end_node = (rows * cols) - 1       # Bottom-Right: (rows-1, cols-1)

        # Iterate through the grid as the water rises
        for time, r, c in flattened:
            curr_idx = r * cols + c
            
            # Look at all 4 adjacent neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    # If the neighbor is already flooded, connect them!
                    if grid[nr][nc] <= time:
                        neighbor_idx = nr * cols + nc
                        union(curr_idx, neighbor_idx)
            
            # The instant the start and end are connected, return the current time
            if find(start_node) == find(end_node):
                return time

        return 0