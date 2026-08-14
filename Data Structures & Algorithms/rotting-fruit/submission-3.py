from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2

        # edge case - empty input
        if not grid:
            return 0 # no fruit = no fresh fruit
        # BFS from rotten fruit

        q = deque()
        # init path to get the start state ie all rotten fruit locations
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                match grid[r][c]:
                    case x if x == FRESH:
                        fresh += 1
                    case x if x == ROTTEN:
                        q.append((r, c))
                    
        # There's no fresh fruit in the input
        if not fresh:
            return 0
        # There's no rotten fruit in the input
        if not q:
            return -1

        # multi bfs
        minutes = 0
        while q:
            if not fresh:
                return minutes
            minutes += 1
            breath = len(q)

            # We process 1 min at a time so we can count
            for rotten in range(breath):
                r, c = q.popleft()

                # for each rotten fruit - do we have an neighbor to rot
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    # look for valid fruit
                    is_valid = (
                        0 <= nr < rows and 0 <= nc < cols # inbounds
                        and grid[nr][nc] == FRESH
                    )

                    if is_valid:
                        grid[nr][nc] = ROTTEN
                        fresh -= 1
                        q.append((nr, nc))
        
        return minutes if not fresh else -1
