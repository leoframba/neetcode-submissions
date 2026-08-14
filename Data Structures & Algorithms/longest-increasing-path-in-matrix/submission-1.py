from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        @cache        
        def dp(r, c) -> int:
            count = 0
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                # bounds
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    count = max(dp(nr, nc), count)

            return count + 1
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(dp(r, c), res)
        return res



        