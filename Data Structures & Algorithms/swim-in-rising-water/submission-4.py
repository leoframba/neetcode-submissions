import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # #start 0,0 and target = (rows - 1, cols - 1)
        # # key = tuple grid cords (r,c) : value [all neighbors in the form (weight, (r, c))]
        # adj = {}
        
        # # N^2 iterate through all nodes to populate my adj dict
        # for r in range(rows):
        #     for c in range(cols):
        #         adj.setdefault((r, c), [])

        # init the distance map with all values at max
        distances = {(r, c): float('inf') for r in range(rows) for c in range(cols)}
        distances[(0,0)] = grid[0][0] # start is always 0 dist from itself

        min_heap = [(grid[0][0], (0, 0))] # (weight, point)

        # keep looking at adjacent points and calc the shortest path from the start
        while min_heap:
            curr_d, curr_n = heapq.heappop(min_heap)
            r, c = curr_n

            if curr_d > distances[(r, c)]:
                continue

            if r == rows - 1 and c == cols - 1:
                return curr_d

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                # bounds check
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_dist = max(curr_d, grid[nr][nc])
                    if new_dist < distances[(nr, nc)]:
                        distances[(nr, nc)] = new_dist
                        heapq.heappush(min_heap, (new_dist, (nr, nc)))

        return distances[(rows - 1, cols - 1)]



               


        