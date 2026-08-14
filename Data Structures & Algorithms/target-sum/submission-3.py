class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # edge cases
        #empty /0 inputs
        if not nums:
            return 0 if target != 0 else 1
        
        
        n = len(nums)

        # dp logic
        # states - curr = the current value of the target, start - the current starting point in the nums list
        # return - # of ways to hit target
        def dp(start: int, curr: int) -> int:
            # wall - 
            # hit the target - return found 1 new valid path
            if start == n:
                return 1 if curr == target else 0 
        
            
            # choice/explore
            # for each number do we add/sub
            combs = dp(start + 1, curr + nums[start]) + dp(start + 1, curr - nums[start])
            # for i in range(start, n):
            #     # add + sub
            #     combs += dp(i + 1, curr + nums[i]) + dp(i + 1, curr - nums[i])
            
            return combs
            

        return dp(0, 0) 
