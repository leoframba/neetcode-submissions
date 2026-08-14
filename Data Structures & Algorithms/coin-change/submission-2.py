# top down recursive apporach

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # cheeky cases
        if amount == 0:
            return 0
        if not coins:
            return -1

        n = len(coins)
        
        # To improve speed we only track the sum of the bag
        res = float('inf')
        
        cache = {}
        # top down approach - we start from the the total and calc what is the best bag for each total
        # return is the total # of coins in the bag
        def dp(remainder) -> int:
            # goal - The last coin we put in the bag allowed us to hit our goal
            if remainder == 0:
                return 0
            
            # wall - The last coin we put in the bag = overshoot
            if remainder < 0:
                return float('inf')
            
            # if we havent calc'd yet
            if remainder not in cache:
                # we must find the min amount of coins
                tot = float('inf')
                for coin in coins:
                    cur = 1 + dp(remainder - coin)
                    if cur < tot:
                        tot = cur
                cache[remainder] = tot

            
            return cache[remainder]

            
            
        

        res = dp(amount)
        print(res)
        return -1 if res == float('inf') else res
        

