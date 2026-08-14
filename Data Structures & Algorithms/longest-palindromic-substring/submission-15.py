from functools import cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # edge case - invalid s
        if not s:
            return ""
        # top down
        # we start from the middle and attempt to expand

        # result tuple holds the bounds of our longest substring
        # defaults to 1 as any valid s will have a plaindrom of at least size 1
        res = (0, 0)

        # state is the bounds of our substring -> return t/f is its a valid palindrome
        def is_pal(left, right):
            while (
                left >= 0 and 
                right < len(s) and 
                s[left] == s[right]
            ):
                nonlocal res
                if right - left + 1 > res[1] - res[0] + 1:
                    res = (left, right)
                left -= 1
                right += 1
            return
        
        
        for i in range(len(s) - 1):
            # at each middle expand

            # attempt to expand itervely from middles
            is_pal(i, i)
            is_pal(i, i + 1) 
            
        
        return s[res[0]: res[1] + 1]
        
        

        