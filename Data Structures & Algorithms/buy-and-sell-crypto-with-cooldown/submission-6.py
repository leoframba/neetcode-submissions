class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # state machine - 3 states rest, hold, sold
        hold = [0 for _ in range(len(prices) + 1)]
        rest = [0 for _ in range(len(prices) + 1)]
        sold = [0 for _ in range(len(prices) + 1)]

        hold[0] = float('-inf')
        for day in range(1, len(prices) + 1):
            #calc each state
            # if we held we must have held prev or bought
            hold[day] = max(hold[day - 1], rest[day - 1] - prices[day - 1])

            # skip / cd
            rest[day] = max(rest[day - 1], sold[day - 1])

            # sold today
            sold[day] = hold[day - 1] + prices[day - 1]
        
        return max(hold[len(prices)], rest[len(prices)], sold[len(prices)])
        