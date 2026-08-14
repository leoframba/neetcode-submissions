from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not t:
            return 1
        
        if not s:
            return 0
        
        slen = len(s)
        tlen = len(t)
        #dp - What is the problem we want to break down?
        # at a given char in s do we take it? 
        @cache
        def dp(sidx, tidx):
            # wall 
            # if we reach the end of our target we have found a valid subseq
            if tidx == tlen:
                return 1
            # we reach the end of our input word - without finding a subseq
            if sidx == slen:
                return 0
            
            # choice - for a given char to we take or skip
            valid_ways = 0
            
            if s[sidx] == t[tidx]:
                valid_ways += dp(sidx + 1, tidx + 1) # take
            valid_ways += dp(sidx + 1, tidx) # skip
            return valid_ways
        
        return dp(0, 0)
        