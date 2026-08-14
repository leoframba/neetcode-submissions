class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rows = len(p)
        cols = len(s)
        
        # DP array sized to the PATTERN (equivalent to a single Column)
        dp = [False] * (rows + 1)
        
        # Base Case 1: Empty matches Empty
        dp[0] = True 
        
        # Base Case 2: Empty string matching stars (e.g., "a*b*")
        for r in range(1, rows + 1):
            if p[r - 1] == '*':
                dp[r] = dp[r - 2]
                
        # FLIPPED LOOPS: Iterate through the String first (moving Col by Col)
        for c in range(1, cols + 1):
            
            # 'prev' acts as our Diagonal (dp[r-1][c-1])
            # For row 1, the diagonal comes from row 0 of the previous column
            prev = dp[0] 
            
            # Once the string has characters, an empty pattern (row 0) ALWAYS fails
            dp[0] = False 
            
            for r in range(1, rows + 1):
                # Save the 'Left' value before we overwrite it!
                temp = dp[r]
                
                if p[r - 1] == '*':
                    # Case 0: Look Up 2 rows (already calculated for THIS column!)
                    case0 = dp[r - 2]
                    
                    # Case 1+: Match the char before the star, and look Left ('temp')
                    match = s[c - 1] == p[r - 2] or p[r - 2] == '.'
                    case1plus = match and temp 
                    
                    dp[r] = case0 or case1plus
                    
                else:
                    # Normal Match: Match the char, and look Diagonal ('prev')
                    match = s[c - 1] == p[r - 1] or p[r - 1] == '.'
                    dp[r] = match and prev
                    
                # The 'Left' value we just saved becomes the 'Diagonal' for the NEXT row down
                prev = temp
                
        return dp[rows]