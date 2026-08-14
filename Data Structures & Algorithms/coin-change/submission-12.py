class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # bottoms up solution

        # edge - 0 amount
        # we assume that input wont allows amount < 0
        if amount == 0:
            return 0
        
        # sort coins - we can prune
        coins.sort() #n log n time
        
        # our base case is 0 amount
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0 # It takes 0 coins to achive an amount 0

        # we will calc all states
        for state in range(1, amount + 1):

            min_coins = amount + 1
            # attempt to reach state from each coin
            for i, coin in enumerate(coins):
                # the first coin we see that goes < 0 we know that we cannot reach this state
                if state - coin < 0:
                    break
                # skip dupes
                if i > 0 and coin == coins[i - 1]:
                    continue    
                
                # this coin + however many it took to get the prev state
                curr = 1 + dp[state - coin]
                min_coins = min(min_coins, curr)
            
            dp[state] = min_coins
        

        return -1 if dp[amount] == amount + 1 else dp[amount] 
                    

        