class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 != 0: 
            return False
            
        target = tot // 2
        
        # dp[i] represents whether we can achieve a subset sum of 'i'
        dp = [False] * (target + 1)
        
        # Base case: We can always achieve a sum of 0 (by picking nothing)
        dp[0] = True 
        
        for num in nums:
            # We MUST iterate backwards to avoid using the same number twice!
            for curr_target in range(target, num - 1, -1):
                # The "Take or Skip" logic boils down to this single line:
                # dp[curr] is True if it was ALREADY True (skip), 
                # OR if the remainder was True (take).
                if dp[curr_target - num] == True:
                    dp[curr_target] = True
                    
            # Early exit optimization: If we hit our target, stop immediately
            if dp[target]:
                return True
                
        return dp[target]