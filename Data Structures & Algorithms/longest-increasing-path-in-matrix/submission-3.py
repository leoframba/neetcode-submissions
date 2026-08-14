from collections import deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])

        depend = {}
        deg = [0 for row in matrix for _ in row]        
        
        # iterate through matrix and build depend map - for each tile we look who depends on
        for r in range(rows):
            for c in range(cols):
                depend.setdefault((r, c), [])
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc

                    # bounds
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[r][c] < matrix[nr][nc]:
                        curr = depend.setdefault((r, c), [])
                        curr.append((nr, nc))
                        deg[nr * cols + nc]+= 1
        
        q = deque()
        for i in range(len(deg)):
            if deg[i] == 0:
                r = i // cols
                c = i % cols
                q.append((r, c))
            



        res = 0
        while q:

            level_size = len(q)
            for _ in range(level_size):
                curr = q.popleft()
                # relax bro
                for r, c in depend[curr]:
                    deg[r * cols + c] -= 1
                    if deg[r * cols + c] == 0:
                        q.append((r, c))
            res += 1
        return res



        


        