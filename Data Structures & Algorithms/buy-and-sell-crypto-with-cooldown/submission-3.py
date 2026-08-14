# bottoms up
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices or len(prices) == 1:
            return 0

        n = len(prices)        
        dp = [[0, 0] for _ in range(n)]

        # base
        dp[0][0] = 0 # we dont start with a stock so we cant sell
        dp[0][1] = -prices[0] # we buy the stock

        # Base Cases (Day 1)
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1]) # Skip or Sell
        dp[1][1] = max(dp[0][1], dp[0][0] - prices[1]) # Hold or Buy
        
        # Iterative Loop
        for i in range(2, n):
            # EMPTY: Skip yesterday's empty, or SELL yesterday's stock
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            
            # HOLDING: Hold yesterday's stock, or BUY today 
            # (must use i-2 empty state for cooldown!)
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
            
        # The max profit will always be on the last day with empty hands
        return dp[n-1][0]

            


        

        