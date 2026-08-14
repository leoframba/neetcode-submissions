class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0
        
        # at a given index do we sell or buy
        cache = {}
        def dp(start, curr) -> int:
            # wall
            if start >= len(prices): 
                return 0

            if (start, curr) in cache:
                return cache[(start, curr)]

            # curr denotes if we are buying/selling. -1 if we need to buy - value of bought coin otherwise
            if curr == -1:
                # buy logic - buy or skip
                skip = dp(start + 1, -1)
                take = dp(start + 1, prices[start])
                cache[(start, curr)] = max(skip, take)
            else:
                # sell logic - sell or hold
                sell = (prices[start] - curr) + dp(start + 2, -1) # cd so we skip one more
                hold = dp(start + 1, curr)
                cache[(start, curr)] = max(sell, hold)
            
            return cache[(start, curr)]
        
        return dp(0, -1)
            

            


        

        