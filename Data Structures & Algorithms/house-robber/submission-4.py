class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp - we only ever care about the last two houses
        # edge case when we calc the first 2 houses looking back outside of the range = robbing empty houses
        rob1 = 0
        rob2 = 0

        # iterate through the houses and calc the cost to rob each one
        for i in range(n):
            curr = max(rob1, rob2 + nums[i])

            rob2 = rob1
            rob1 = curr
        
        return rob1
            

        