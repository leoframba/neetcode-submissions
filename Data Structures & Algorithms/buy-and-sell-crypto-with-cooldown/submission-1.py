from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0
        
        
        # at a given index do we sell or buy
        @cache
        def dp(start, curr) -> int:
            # wall
            if start >= len(prices): 
                return 0

            # if but is true we need to buy
            # ? do we buy this value or skip
            
            if curr == -1:
                # buy logic - buy or skip
                skip = dp(start + 1, -1)
                take = dp(start + 1, prices[start])
                return max(skip, take)
            else:
                # sell logic - sell or hold
                sell = (prices[start] - curr) + dp(start + 2, -1) # cd so we skip one more
                hold = dp(start + 1, curr)
                return max(sell, hold)
        
        return dp(0, -1)
            

            


        

        