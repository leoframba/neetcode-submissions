class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # edge cases
        # either input is not valid
        if not text1 or not text2:
            return 0
        # same word
        if text1 == text2:
            return len(text1)
        
        # bottoms up

        rows = len(text1)
        cols = len(text2)
        # base case = end of string
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                # match
                if text1[r - 1] == text2[c - 1]:
                    dp[r][c] = 1 + dp[r - 1][c - 1]
                else:
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
        
        # back track
        r = rows
        c = cols
        ss_len = dp[r][c]
        res = []
        while ss_len > 0:
            # check if we came from a match
            if text1[r - 1] == text2[c - 1]:
                res.append(text1[r - 1])
                r -= 1
                c -= 1
                ss_len -= 1
            else:
                # we came from max of up or left
                left = dp[r][c - 1]
                up = dp[r - 1][c]
                if left >= up:
                    c -= 1
                else:
                    r -= 1
        
        res = "".join(res)
        print(res)
        return len(res)