from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return len(nums)

        @cache
        def dp(start, last_val) -> int:
            # base - end of list
            if start >= len(nums):
                return 0
            
            # at any given number we can
            #if the value is greater than the last one we can add it to our current sub
            
            cont = float('-inf')
            if last_val < nums[start]:
                cont = 1 + dp(start + 1, nums[start])

            skip = dp(start + 1, last_val)    
            
            return max(cont, skip)
        
        return dp(0, float('-inf'))
                
        