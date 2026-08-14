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
        has_land = False
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == TREASURE:
                    q.append((r, c))
                if grid[r][c] == LAND:
                    has_land = True
        if not q or not has_land:
            return None
        
        # bfs from each chest as soon as we find a land we know its the min
        dst = -1
        while q:
            dst += 1
            level = q
            q = deque()
            while level:
                r, c = level.popleft()
                
                # search
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    is_valid = (
                        0 <= nr < rows and 0 <= nc < cols # in bounds
                        and grid[nr][nc] == LAND
                    )
                    if is_valid:
                        grid[nr][nc] = dst + 1
                        q.append((nr, nc))
        return

        
        