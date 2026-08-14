class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        
        # rows = t cols = s
        rows = len(t) + 1
        cols = len(s) + 1
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        # base case
        for c in range(cols):
            dp[0][c] = 1 # two empty strings are a valid match

        for r in range(1, rows):
            for c in range(1, cols):
                # if the current vals match we check r-1 c-1
                if t[r - 1] == s[c - 1]:
                    dp[r][c] += dp[r-1][c-1]
                dp[r][c] += dp[r][c-1]
        
        return dp[rows - 1][cols - 1]

        
        