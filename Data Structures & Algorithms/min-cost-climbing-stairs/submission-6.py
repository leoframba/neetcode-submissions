class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # using an iterative bottoms up approach we can achive constant space


        # we can start from step 2(index 1)
        dp = [0] * len(cost)

        # the first two stairs are solved as we can jump from the start to step 1/2

        for i in range(2, len(cost)):

            #solving for step i - to get here we can jump from i - 2 or i - 1
            dp[i] = min(
                cost[i - 2] + dp[i - 2], # we can jump 2 from i-2 for the cost of getting there + its cost
                cost[i - 1] + dp[i - 1] # "" but from 1
            )

        return min(dp[-1] + cost[-1], dp[-2] + cost[-2])
            

            


        