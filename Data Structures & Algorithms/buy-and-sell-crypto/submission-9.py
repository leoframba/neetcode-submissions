class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force - we can loop throught the array and check buy/sell at any given point

        n = len(prices)

        res = 0
        for i in range(n):
            buy = prices[i]
            for k in range(i + 1, n):
                sell = prices[k]
                if sell > buy:
                    # attempt to sell
                    res = max(res, sell - buy)
        
        return res




        