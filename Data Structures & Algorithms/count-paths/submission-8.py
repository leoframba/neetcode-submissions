from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # brute force dfs

        # at any given state we can go down or right
        # if we reach the goal m - 1 n - 1 we have a valid path

        # we return an int for valid path or not
        @cache
        def dfs(r: int, c: int) -> int:
            # base case - we hit the target
            if r == m - 1 and c == n - 1:
                return 1
            
            # base case - we are out of bounds
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            
            # we are at a valid state
            # from each state we attempt to go down or right

            down = dfs(r + 1, c)
            right = dfs(r, c + 1)
            return down + right
        
        return dfs(0, 0)
    
    # Brute force at each point we are running dfs which can go down or right
    # so 2^m*n