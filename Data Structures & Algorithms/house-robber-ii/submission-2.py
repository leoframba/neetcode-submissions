from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        # A completely isolated universe builder!
        def rob_universe(start_idx, end_idx):
            memo = {} # Fresh memo every time this is called!
            
            def dp(i):
                # Base Case: If we step past our designated start line
                if i < start_idx:
                    return 0
                    
                if i not in memo:
                    # Your exact, flawless recurrence relation
                    memo[i] = max(nums[i] + dp(i - 2), dp(i - 1))
                    
                return memo[i]
                
            # Start the recursion from the end of this specific universe
            return dp(end_idx)

        # Universe A: Include House 0, completely ignore the last house
        universe_a = rob_universe(0, n - 2)
        
        # Universe B: Completely ignore House 0, include the last house
        universe_b = rob_universe(1, n - 1)

        return max(universe_a, universe_b)