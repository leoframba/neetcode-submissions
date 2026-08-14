from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # edge case - empty input - a empty gird has no islands
        if not grid:
            return 0

        # start with a bfs approach where we measure size

        rows, cols = len(grid), len(grid[0])

        visited = set()
        island_count = 1

        # takes cords and returns total size of bfs
        def bfs(r: int, c: int) -> int:
            # defence - check input is inbounds
            inbounds = (0 <= r < rows and 0 <= c < cols)
            if not inbounds:
                return 0
            
            start_state = (r, c)
            visited.add(start_state)
            q = deque([start_state])
            area = 0

            while q:
                r, c = q.popleft()
                area += 1

                # search
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    # Only procces valid adj lands
                    is_valid = (
                        (0 <= nr < rows and 0 <= nc < cols) # inbounds
                        and grid[nr][nc] == 1 # is a land
                        and (nr, nc) not in visited # has not been visited already 
                    )
                    if is_valid:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            
            return area

        max_area = 0
        # iterate over the grid and preform bfs when we see an unvisited island
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area
        

        

        