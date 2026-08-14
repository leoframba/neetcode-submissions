from functools import cache
class Solution:
    def longestPalindrome(self, s: str) -> str:

        # top down
        # we start from the middle and attempt to expand

        # result tuple holds the bounds of our longest substring
        # defaults to 1 as any valid s will have a plaindrom of at least size 1
        res = (0, 0)

        # state is the bounds of our substring -> return t/f is its a valid palindrome
        def dp(left, right) -> bool:
            # base case - we are out of bounds
            # out of bounds = invalid
            if left < 0 or right >= len(s):
                return False
            
            # if we are inbounds we check if these chars are a match
            if s[left] == s[right]:
                nonlocal res
                # set - we could also pull this from the states?
                if right - left + 1 > res[1] - res[0] + 1:
                    res = (left, right)
                # keep looking
                return dp(left - 1, right + 1)
            else:
                return False
        
        for i in range(len(s) - 1):
            # at each middle expand

            # due to even palis we need to expand from i + 1 asell
            dp(i, i)
            dp(i, i + 1)
        
        return s[res[0]: res[1] + 1]
        
        

        