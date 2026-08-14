class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # edge
        if not text1 or not text2: 
            return 0 
        
        #dp approach split into smaller problems
        # smaller of the two is the target

        cache = {}
        def dp(s1, s2) -> int:
            # wall - weve reached the end
            if s1 == len(text1) or s2 == len(text2):
                return 0
            
            if (s1, s2) in cache:
                return cache[(s1, s2)]
            
            # if both words have the same char move both
            if text1[s1] == text2[s2]:
                cache[(s1, s2)] = 1 + dp(s1 + 1, s2 + 1)
                return cache[(s1, s2)]
            else:
                # we try both
                cache[(s1, s2)] = max(dp(s1 + 1, s2), dp(s1, s2 + 1))
                return cache[(s1, s2)]
            
            cache[(s1, s2)] = 0
            return 0

        return dp(0, 0)
        