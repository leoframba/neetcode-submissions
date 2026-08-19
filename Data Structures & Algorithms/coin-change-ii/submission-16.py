class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
                # top down

        #edge
        # we can always achive 0 with 0 coins
        if amount == 0:
            return 1
        
        # no coins no solutions
        if not coins:
            return 0
        
        # sort coins to prune
        coins.sort()
        while coins and coins[-1] > amount:
            coins.pop()
        
        # Create an amount list where amount[i] = T/F we can achive this value
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1 # we can always make the amount 0

        for c in coins:
            for target in range(1, amount + 1):
                if target - c < 0:
                    continue
                if dp[target - c] > 0:
                    dp[target] += dp[target - c]

        print(dp)
        return dp[amount]

        