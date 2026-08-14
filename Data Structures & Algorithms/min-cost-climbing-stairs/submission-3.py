class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        n = len(cost)

        cache = {}
        def dp(i):
            if i >= n:
                return 0
            
            if i in cache:
                return cache[i]
            
            #choice 1 step or two - we want the one with the min cost
            choice = min(dp(i + 1), dp(i + 2))
            cache[i] = choice + cost[i]

            return choice + cost[i]
        
        # we can start from either the first or 2nd step
        return min(dp(0), dp(1))



        