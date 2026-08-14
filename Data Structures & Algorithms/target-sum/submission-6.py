class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        # Edge Case 1: The target is completely out of reach
        if abs(target) > total:
            return 0
            
        # Edge Case 2: The math gives us a decimal (e.g., target 3, total 4 -> 7/2 = 3.5)
        # We can't reach a decimal sum with integers, so it's impossible.
        if (target + total) % 2 != 0:
            return 0
            
        # Our new goal: Find subsets that sum to this exact positive number
        subset_target = (target + total) // 2
        
        # 1D DP Array Setup (Exactly like Coin Change 2)
        dp = [0] * (subset_target + 1)
        dp[0] = 1 # 1 way to make a sum of 0
        
        for num in nums:
            # We iterate BACKWARDS exactly like Partition Equal Subset Sum
            # to ensure we only use each number once!
            for t in range(subset_target, num - 1, -1):
                dp[t] += dp[t - num]
                
        return dp[subset_target]