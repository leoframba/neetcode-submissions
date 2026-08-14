class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) == 0:
            return 0

        for i in range(len(prices)):
            for k in range( i + 1, len(prices)):
                curr = prices[k] - prices[i]
                profit = max(curr, profit) 
         
        return profit

        