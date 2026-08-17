from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #edge case
        if not prices:
            return 0
        
        
        # each day we can buy/sell/hold + cd
        @cache
        def dp(day, hold: bool) -> int:
            # base case 
            if day >= len(prices):
                return 0
            
            buy = 0
            sell = 0
            # each day we can buy or sell or hold
            #sell
            if hold:
                sell = prices[day] + dp(day + 2, False)
            #buy - we can only buy one stock at a time 
            else:
                buy = dp(day + 1, True) - prices[day]

            hold = dp(day + 1, hold)

            return max(buy, sell, hold)
        
        return dp(0, False)


        