from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        #edge cases
        # empty inputs
        if not s and not p:
            return True
        
        
        plen = len(p)
        slen = len(s)
        @cache
        def dp(si, pi):
            # wall
            # if we reach the ends of both the pattern and string we've matched
            if pi == plen:
                return si == slen
                    
            
            # choice - how to consume chars
            # we need to look ahead for * char

            # True if the next char i p is a start
            match = si < slen and (s[si] == p[pi] or p[pi] == '.')
            star = pi + 1 < plen and p[pi + 1] == '*'

            # no star
            if not star:
                return match and dp(si + 1, pi + 1)
            else:
                #start can be 0. No match so we must +2 to skip cur p + star
                case0 = dp(si, pi + 2) 
                case1plus = match and dp(si + 1, pi) #iterate only the s index as star allows or more of the p ele
                return case0 or case1plus

        return dp(0, 0)
        