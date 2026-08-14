class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # edge cases
        if m == 0 and n == 0:
            return 0
        
        cache = [[-1 for _ in range(n)] for _ in range(m)]

        # at every tile we have two steps down or right
        def dp(x, y) -> int:
            # wall - out of bounds or reached the goal
            if x >= m or y >= n:
                return 0 # 0 bc this is not a valid path
            if x == m - 1 and y == n -1:
                return 1 # valid path
            
            if cache[x][y] != -1:
                return cache[x][y]
            
            # down
            down = dp(x, y + 1)

            # right
            right = dp(x + 1, y)

            
            cache[x][y] = down + right
            return cache[x][y]

        
        return dp(0, 0)

        