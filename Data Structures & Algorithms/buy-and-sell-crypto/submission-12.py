from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        n = len(prices)

        # at any index we can buy/sell
        @cache
        def dp(i, buy_price) -> int:
            # wall - end of the list
            if i >= n:
                return 0
            
            #calc the current val
            profit = prices[i] - buy_price

            # at any given day we can skip or buy the current stock
            # if the current stock is cheaper we can consider buying it
            buyorskip = 0
            if prices[i] < buy_price:
                buyorskip = dp(i + 1, prices[i])
            else:
                # if our current buy is lower we keep it
                buyorskip = dp(i + 1, buy_price)

            return max(profit, buyorskip)

        
        # start off assuming we buy prices[0]
        return dp(1, prices[0])
        