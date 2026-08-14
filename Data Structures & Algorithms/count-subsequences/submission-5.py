class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        if len(s) < len(t):
            return 0
        # rows = t cols = s
        rows = len(t) + 1
        cols = len(s) + 1
        dp = [0 for _ in range(cols)]
        # base case
       
        dp[0] = 1 # two empty strings are a valid match

        
        for c in range(1, cols):
            for r in range(rows - 1, 0,  -1):
                # if the current vals match we check r-1 c-1
                if t[r - 1] == s[c - 1]:
                    dp[r] += dp[r-1]
        
        return dp[rows - 1]

        
        