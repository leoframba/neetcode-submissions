class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # double empty
        if not s and not p:
            return True
        
        # empty string is ok bc * pattern can match
        if not p:
            return False
        
        rows = len(p)
        cols = len(s)
        dp = [[False] * (cols + 1) for _ in range(rows + 1)]
        dp[0][0] = True
        for r in range(1, rows + 1):
            star = r + 1 < rows + 1 and p[r] == '*'
            dp[r][0] = star or p[r - 1] == '*'

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if p[r - 1] == '*':
                    dp[r][c] = dp[r - 1][c]
                    continue

                # what do we need to handle
                match = s[c - 1] == p[r - 1] or p[r - 1] == '.'
                star = r + 1 < rows + 1 and p[r] == '*'

                dp[r][c] = False
                if star:
                    dp[r][c] = (match and dp[r][c - 1]) or dp[r - 1][c]
                else:
                    dp[r][c] = match and dp[r - 1][c - 1]
        
        return dp[rows][cols]
                
        
        