class Solution:
    def climbStairs(self, n: int) -> int:

        # bottom up

        # only need to hold the last two states
        # state for 1 - only 1 way 1 step to get to one
        prev = 1
        # two ways to get to state 2 1+1 or 2
        curr = 2

        if n < 0:
            return None
        if n <= 1:
            return prev
        #state 3 = stat 1 + state 2
        # we need to calc state n

        for i in range(2, n):
            curr, prev = curr + prev, curr
        
        return curr


        
            


        
        