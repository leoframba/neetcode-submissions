class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        #top down
        memo = {}

        def dp(i):
            if i < 0:
                return 0

            if i not in memo:
                memo[i] = max(nums[i] + dp(i - 2), dp(i - 1))
            
            return memo[i]

        
        return dp(n - 1) 

        