from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # edge cases - assume no 0 or negative
        if amount <= 0:
            return 1
        
        # no coins :(
        if not coins:
            return 0

        # Quick viability check
        if amount < min(coins):
            return 0
        
        coins.sort() # n log n

        # curr = current amount, start = coins index
        @cache
        def dp(curr, start) -> bool:
            # hit target
            if curr == 0:
                return 1
            # overshot
            if curr < 0:
                return 0 
            # Out of coins
            if start >= len(coins):
                return 0
            
            take = 0
            for i in range(start, len(coins)):
                if curr - coins[i] < 0:
                    break
                else:
                    take += dp(curr - coins[i], i)

            # take = dp(curr - coins[start], start)
            # skip = dp(curr, start + 1)
            
            return take
        
        return dp(amount, 0)
                

        