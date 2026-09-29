from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        # options
        # buy stock
        # sell stock
        # hold stock
        
        @cache
        def dp(day, stock):
            # base case
            if day >= len(prices):
                return 0
            
            sell = 0
            buy = 0
            if stock:
                # we are holding a stock we can sell it
                sell = dp(day + 1, 0) + prices[day]
            else:
                buy = dp(day + 1, 1) - prices[day]
                    
            skip = dp(day + 1, stock)
            return max(skip, buy, sell)
        
        return dp(0, 0)
                






        