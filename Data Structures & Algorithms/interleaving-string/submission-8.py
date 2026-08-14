class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        #edge cases
        
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        # we cannot create len3 if we dont have enough chars
        if len3 != len1 + len2:
            return False

        dp = [[False for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        # build base
        dp[0][0] = True # empty empty == empty
        # set base for cols = s2
        for i in range(1, len2 + 1):
            dp[0][i] = s2[i-1] == s3[i-1]
            if not dp[0][i]:
                break
        # set base for rows = s1
        for i in range(1, len1 + 1):
            dp[i][0] = s1[i-1] == s3[i-1]
            if not dp[i][0]:
                break
        

        for r in range(1, len1 + 1):
            for c in range(1, len2 + 1):
                # do we have a valid path inc
                dp[r][c] = dp[r-1][c] and s1[r - 1] == s3[r + c - 1] or (dp[r][c-1] and s2[c-1] == s3[r + c - 1])

        return dp[len1][len2]



        
        