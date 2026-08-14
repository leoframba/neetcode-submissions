from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # edge
        if not text1 or not text2: 
            return 0 
        
        #dp approach split into smaller problems
        # smaller of the two is the target

        @cache
        def dp(s1, s2, l) -> int:
            if s1 == len(text1):
                return 0
            if s2 == len(text2):
                return 0
            
            # if both words have the same char move both
            if text1[s1] == text2[s2]:
                return 1 + dp(s1 + 1, s2 + 1, l + 1)
            else:
                # we try both
                return max(dp(s1 + 1, s2, l), dp(s1, s2 + 1, l))
            
            return 0

        return dp(0, 0, 0)
        