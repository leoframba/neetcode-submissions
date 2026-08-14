class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad the array with 1s (our permanent walls)
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[left][right] = max coins strictly between left and right
        dp = [[0] * n for _ in range(n)]
        
        # 1. Expand the window length from 2 up to n - 1
        for length in range(2, n):
            
            # 2. Slide the left wall across the array
            # It stops early enough so the right wall doesn't go out of bounds
            for left in range(n - length):
                
                # The right wall is mathematically locked to the left wall
                right = left + length
                
                # 3. Try every balloon inside the window as the LAST to pop
                for i in range(left + 1, right):
                    
                    coins = nums[left] * nums[i] * nums[right]
                    total = dp[left][i] + dp[i][right] + coins
                    
                    dp[left][right] = max(dp[left][right], total)
                    
        # Return the max coins for bursting everything strictly between the padded 1s
        return dp[0][n - 1]