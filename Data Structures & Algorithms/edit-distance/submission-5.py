class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        len1 = len(word1) # cols
        len2 = len(word2) # rows

        
        dp = [[0 for _ in range(len1 + 1)] for _ in range(len2 + 1)]
        # base case - comparing an empty w1 or w2 = insert all or delete all
        # row 0
        for c in range(1, len1 + 1):
            dp[0][c] = c
        # col 0
        for r in range(1, len2 + 1):
            dp[r][0] = r
        
        for r in range(1, len2 + 1):
            for c in range(1, len1 + 1):
                # 4 outcomes we take the option with the min
                ops = float('inf')
                # if the curr chars are equal we can look diag for free
                if word1[c - 1] == word2[r - 1]:
                    ops = min(ops, dp[r-1][c-1])
                else:
                    # we must preform an action
                    ops = min(ops, dp[r-1][c-1] + 1) # replace
                    ops = min(ops, dp[r][c-1] + 1) # delete
                    ops = min(ops, dp[r-1][c] + 1) # replace
                dp[r][c] = ops
        
        return dp[len2][len1]


        

         