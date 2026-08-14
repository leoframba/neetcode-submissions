from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        TREASURE = 0
        LAND = 2 ** 31 - 1
        WATER = -1
        
        if not grid:
            return None
        
        # bfs from chests -> lands
        rows, cols = len(grid), len(grid[0])
        
        q = deque()
        # get the location of every chest
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == TREASURE:
                    q.append((r, c))
        
        # bfs from each chest as soon as we find a land we know its the min
        dst = -1
        visited = {state for state in q}
        while q:
            dst += 1
            level = q
            q = deque()
            while level:
                r, c = level.popleft()
                
                # dst is increasing so the first time we see a land we know its the min dst
                if grid[r][c] == LAND:
                    grid[r][c] = dst
                
                # search
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    is_valid = (
                        0 <= nr < rows and 0 <= nc < cols # in bounds
                        and (nr, nc) not in visited
                        and grid[nr][nc] == LAND
                    )
                    if is_valid:
                        visited.add((nr, nc))
                        q.append((nr, nc))
        return






        
        