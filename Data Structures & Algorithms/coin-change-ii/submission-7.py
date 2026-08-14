# bottoms up

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        #edge cases
        # empy inputs/0
        if amount == 0:
            return 1
        
        if not coins:
            return 0
        
        # dp matrix
        # states = amount/coins

        # row = amount and col will be the valid number of combos
        r_len = amount + 1
        c_len = len(coins) + 1

        # define the dp matrix - all coins can make one combo at row 0 by doing nothing
        dp = [[0 for _ in range(c_len)] for _ in range(r_len)]
        for i in range(c_len):
            dp[0][i] = 1  
        
        # we do one coin at a time like in top down we dont "look back" once we've delt with one coin
        for c in range(1, c_len):
            for r in range(1, r_len):
                coin = coins[c - 1] # index -1 to remove buffer
                # at any given time the row we are on is the target amount
                # we look left to see what combos we've found on prev runs and look back the value of the coin to see new combos
                dp[r][c] = dp[r][c - 1] # always take the # of combos prev found
                # bounds check
                if r - coin >= 0:
                    dp[r][c] += dp[r - coin][c] 
        
        return dp[r_len - 1][c_len - 1]




            


        