class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) == 0:
            return 0

        low = float('inf')
        for i in range(len(prices)):
            low = min(low, prices[i])

            if prices[i] > low:
                profit = max(profit, prices[i] - low)
                
         
        return profit

        