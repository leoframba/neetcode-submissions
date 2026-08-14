from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad the array with 1s to act as our permanent outer walls
        nums = [1] + nums + [1]
        
        # dp(left, right) returns the max coins obtained by bursting all balloons 
        # STRICTLY BETWEEN index 'left' and index 'right'.
        @cache
        def dp(left, right):
            # Wall: If there are no balloons strictly between left and right
            if left + 1 == right:
                return 0
                
            max_coins = 0
            
            # 'i' represents the balloon we choose to pop LAST in this interval
            for i in range(left + 1, right):
                
                # Because 'i' is the last to pop, it merges with the solid walls 
                # at 'left' and 'right' when it finally bursts.
                coins_for_last_pop = nums[left] * nums[i] * nums[right]
                
                # The total is the cost of popping everything on its left, 
                # plus everything on its right, plus the final pop itself.
                total = dp(left, i) + dp(i, right) + coins_for_last_pop
                
                max_coins = max(max_coins, total)
                
            return max_coins
            
        # We want to burst everything strictly between the padded 1s
        return dp(0, len(nums) - 1)