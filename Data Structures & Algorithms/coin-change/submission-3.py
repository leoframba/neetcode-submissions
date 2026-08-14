# bottoms up approach

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # same base cases
        if amount == 0:
            return 0
        if not coins:
            return -1
        
        n = len(coins)

        cache = {i : float('inf') for i in range(1, amount + 1)}
        for i in range(1, amount + 1):
            
            # goal is to calc the min # of coins to reach amount == i
            for coin in coins:
                # if the coin overshoots we cant use it
                if i - coin < 0:
                    continue
                # if we can reduce the amount to 0 with the current coin we say 1
                if i - coin == 0:
                    cache[i] = min(1, cache[i])
                else:
                    # if the coin reduces the val we add it to the soltion of the val
                    cache[i] = min(1 + cache[i - coin], cache[i])
            
        return -1 if cache[amount] == float('inf') else cache[amount]
                
                
                





        