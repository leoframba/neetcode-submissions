class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        # edge - 0 amount
        # we assume amount cannot be < 0
        if amount == 0:
            return 0
        
        # edge - empty coins
        # we assume coins cannt be empty

        
        # sort + prune
        coins.sort() #nlogn
        while coins and coins[-1] > amount:
            coins.pop()

        
        # top down dp approach
        # tot: remaining total -> return # of coins
        cache = [-1] * (amount + 1)
        def dp(tot: int) -> int:
            # base case
            if tot == 0:
                return 0
            if tot < 0:
                return amount + 1
            
            if cache[tot] != -1:
                return cache[tot]

            min_coins = amount + 1
            for i in range(len(coins)):
                if tot - coins[i] < 0:
                    break
                min_coins = min(min_coins, 1 + dp(tot - coins[i]))
            
            cache[tot] = min_coins
            return min_coins
            
        res = dp(amount)
        return -1 if res == amount + 1 else res

        