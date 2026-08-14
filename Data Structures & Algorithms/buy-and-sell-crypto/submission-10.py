class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sliding windows
        buy = 0
        res = 0
        n = len(prices)
        for sell in range(1, n):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                curr = prices[sell] - prices[buy]
                res = max(curr, res)
        
        return res

            






        