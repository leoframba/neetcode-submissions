class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        # dp doesnt work in a circle 
        # WEe have two situations - take house 1 and dont take last or dont take 1 and get last
        # if we take nums[0] -> n-2
        # if we dont take nums[0] -> n - 1

        def dp(costs, i):
            if i < 0:
                return 0

            if i in memo:
                return memo[i]

            # curr vs opp cost
            memo[i] = max(costs[i] + dp(costs, i - 2), dp(costs, i - 1))
            return memo[i]
        
        def help():
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            c1 = dp(nums[1:], n - 2)
            memo.clear()
            return max(c1, dp(nums, n - 2))
            
            

        return help()
        