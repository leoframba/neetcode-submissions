class Solution:
    def numDecodings(self, s: str) -> int:
        # bottoms up approach

        # for each bite we calc the number of substrings up until that point

        # we keep track of two states
        prevprev = 0 # state where we jumped 2
        prev = 1 # state where we jumped 1

        
        idx = len(s) - 1
        while idx >= 0:
            
            tot = 0
            # adds nothing to the total
            if s[idx] != '0':
                tot += prev
                # numbers that start with 1/2 are valid for double digit encoding
                if idx + 1 < len(s):
                    double = int(s[idx:idx + 2])
                    if 10 <= double <= 26:
                        tot += prevprev
            
        
            prevprev = prev
            prev = tot
            idx -= 1
        
        return prev
            

                



            




        