class Solution:
    def climbStairs(self, n: int) -> int:

        
        if n < 0:
            return None
        if n <= 2:
            return n
        
        #too make sure we calc each val once only we use a cache
        cache = {}
        # curr is the current val
        # returns 1 if we reach 0 = valid combination
        def dp(curr: int) -> int:
            # wall
            # valid path found
            if curr == 0:
                return 1
            # overshot
            if curr < 0:
                return 0
            
            if curr in cache:
                return cache[curr]

            # we can take step 1 or 2
            tot = dp(curr - 2) + dp(curr - 1)
            cache[curr] = tot
            return tot

        return dp(n)
        
        