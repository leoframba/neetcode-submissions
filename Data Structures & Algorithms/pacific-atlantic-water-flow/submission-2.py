from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # Two set approach with multi bfs

        if not heights or not heights[0]:
            return []
        
        # set of tiles that can reach the pacific ocean
        # we start with the vals adj to pacific
        rows, cols = len(heights), len(heights[0])
        p_set = set()
        a_set = set()

        for c in range(cols):
            p_set.add((0, c))
            a_set.add((rows - 1, c))
        for r in range(rows):
            p_set.add((r, 0))
            a_set.add((r, cols - 1))
        
        # modifies start_state to include all values post bfs
        def bfs(start_state) -> None:
            if not start_state:
                return

            q = deque(start_state)
            while q:
                r, c = q.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    is_valid = (
                        0 <= nr < rows and 0 <= nc < cols
                        and heights[nr][nc] >= heights[r][c]
                        and (nr, nc) not in start_state
                    )

                    if is_valid:
                        start_state.add((nr, nc)) # p_set can now reach this tile
                        q.append((nr, nc))

       
        bfs(p_set)
        bfs(a_set)
        
        intersect =  p_set.intersection(a_set)
        return list(intersect) if intersect else []


        