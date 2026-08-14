from functools import cache

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # # base cases for cheeky inputs
        # if not s:
        #     return 0
        # if n == 1:
        #     return 1
        # dp = {}
        @cache
        def is_pali(left, right):
             

            # check bounds
            if left >= right:
                return True 

            if s[left] == s[right]:
                return is_pali(left + 1, right -1) # if the outer vals are pali we must check inward
                
            return False
        
        count = 0
        for i in range(n):
            for j in range(i, n):
                if is_pali(i, j):
                    count += 1
        return count
            



        