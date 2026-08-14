class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        decode = {str(i + 1): chr(ord('A') + i) for i in range(26)}

        # we can break the problem down in a two step prob given that we can only decode at most two nums
        # for a given substring how many decodings can we produce 0 - 2
        memo = {}

        def dp(start) -> int: # returns 0 - 2 based on the # of codes
            if start == n:
                return 1
            
            # cant start a code with 0
            if s[start] == "0":
                return 0
            
            # We can choose to consume 1 or 2 chars
            # no bounds check here beacuse we have a start == n check
            if start not in memo:
                memo[start] = dp(start + 1) # Only one cahr bc +1

                #or
                #bounds check
                if start + 1 < n and s[start: start + 2] in decode:
                    memo[start] += dp(start + 2)
            
            return memo[start]
        
        return dp(0)
            



        