from functools import cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # palindrome = string that is the same front and back
        dp = {}
        @cache
        def is_pal(l: int, r: int) -> bool:
            if l > r:
                return True
            
            if s[l] == s[r]:
                return is_pal(l + 1, r - 1)
            else:
                return False
        
        # edge cases
        # empty string
        if not s:
            return []
        
        res = []
        # index + current partition
        def rec(start, curr):
            # wall - base
            # end of input - we have succesfully split the arry into palis
            if start >= len(s):
                res.append(curr.copy())
                return
            
            for i in range(start, len(s)):
                # find a palindrome
                # get current slic
                if start == i or is_pal(start, i):
                    # we can take it
                    curr.append(s[start:i+1])
                    rec(i + 1, curr)
                    #backtrack
                    curr.pop()
                # if we dont find a pall we do nothing
            
            return
        
        rec(0, [])
        return res
        




        