from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        #edge cases
        # empy inputs/0
        if amount == 0:
            return 1
        
        if not coins:
            return 0
        
        n = len(coins)
        
        # top down dp - start with tot and reduce per coin taken -> 0
        # goal per state calc if a valid combination to reach target
        # key = reminader : value = number of possible combos from this remiander
        @cache
        def dp(remainder: int, start: int) -> int: 
            # wall - we hit 0 = valid combo or overshoot = invalid
            # valid combo found return 1
            if remainder == 0:
                return 1
            #invalid we over shot
            if remainder < 0:
                return 0
            # we are at the end of our bag
            if start == n:
                return 0


            # explore/choice at each given remainder look at all coins
            combs = 0
            for i in range(start, n):
                combs += dp(remainder - coins[i], i)
            
            return combs

        #result = total number of combinations
        return dp(amount, 0)

        