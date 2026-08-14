from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # edge cases
        # empty input
        if not nums:
            return 0
        
        # we 
        n = len(nums)
        if n == 1:
            return nums[0] # only one ball to pop
        
        # Problem? 
        @cache
        def dp(curr):
            curr = list(curr)
            # wall - no more balls to pop
            clen = len(curr)
            if clen == 0:
                return 0
            
            # choice which ball to pop
            coins = float('-inf')
            for i in range(clen):
                nl = 1 if i - 1 < 0 else curr[i - 1]
                nr = 1 if i + 1 >= clen else curr[i + 1]
                tot = curr[i] * nl * nr
                coins = max(coins, tot + dp(tuple(curr[:i] + curr[i + 1:])))
            return coins
        return dp(tuple(nums))




        