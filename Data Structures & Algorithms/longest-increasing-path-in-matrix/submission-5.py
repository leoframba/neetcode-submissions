class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        # 1. Flatten the matrix into a list of (value, row, col)
        cells = []
        for r in range(rows):
            for c in range(cols):
                cells.append((matrix[r][c], r, c))
                
        # 2. Sort the cells in ASCENDING order based on value
        cells.sort(key=lambda x: x[0])
        
        # 3. Initialize DP table (every cell is at least a path of length 1)
        dp = [[1] * cols for _ in range(rows)]
        max_path = 1
        
        # 4. Process cells strictly from smallest to largest
        for val, r, c in cells:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                # If the neighbor is strictly smaller, we can extend its path!
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] < val:
                    dp[r][c] = max(dp[r][c], 1 + dp[nr][nc])
                    
            max_path = max(max_path, dp[r][c])
            
        return max_path