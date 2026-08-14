from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        
        # we need to find all valid substrings for a given input
        # valid substrings can be 1 or two digits

        # edge case - empty input
        if not s:
            return 0
        
        #edge case - invalid input - non numerical
        try:
            int(s)
        except ValueError:
            return 0
        
        # We break down our problem into base cases - base case is when its valid

        @cache
        def dp(start) -> int:
            #wall - base case we have reached the end of the string proccesing eveything
            if start >= len(s):
                return 1

            # We can either proccess one digit or two
            ss = s[start: start + 2]
            # check for 0
            if ss[0] == '0':
                return 0 # invalid decode
            
            
            tot = 0
            
            val = int(ss)
            # can we decode as a 2 digit?
            if 10 <= val <= 26:
                tot += dp(start + 2)
            
            # we can always decode a single as we prune 0's
            tot += dp(start + 1)

            return tot

                



            

            
            
            return tot
        
        return dp(0)



            



    