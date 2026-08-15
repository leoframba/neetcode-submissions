from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # edge cases
        # either input is not valid
        if not text1 or not text2:
            return 0
        # same word
        if text1 == text2:
            return len(text1)

        # state = two pointers one for each text
        @cache
        def dp(i1: int, i2: int) -> int:
            # base case - end of string
            if i1 >= len(text1) or i2 >= len(text2):
                return 0
            
            # options
            # match - the pointers are at two matching chars
            # can only take this branch if we have a match
            match = 0
            if text1[i1] == text2[i2]:
                match = 1 + dp(i1 + 1, i2 + 1)
            
            move1 = dp(i1 + 1, i2)
            move2 = dp(i1, i2 + 1)

            # We want the branch with the longest
            return max(match, move1, move2)
        
        return dp(0, 0)