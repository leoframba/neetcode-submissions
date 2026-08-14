class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # edge
        if not text1 or not text2: 
            return 0 
        
        #dp approach split into smaller problems
        # smaller of the two is the target
        rows = len(text1)
        cols = len(text2)

        # a tile in the grid will represent the longest subseq at that stage
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if text1[r - 1] == text2[c - 1]:
                    dp[r][c] = 1 + dp[r - 1][c - 1]
                else:
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
        
        print(dp)
        return dp[rows][cols]
        