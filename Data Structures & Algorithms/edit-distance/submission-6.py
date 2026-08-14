class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        
        # Sized to word1 (columns)
        dp = [c for c in range(len1 + 1)]
        
        for r in range(1, len2 + 1):
            # At the start of a new row, the 'Above' value of the 0th cell
            # becomes the 'Diagonal' for the 1st cell.
            prev = dp[0]
            dp[0] = r # Update column 0 base case
            
            for c in range(1, len1 + 1):
                # 1. Save the pristine 'Above' value before we overwrite it
                temp = dp[c]
                
                if word1[c - 1] == word2[r - 1]:
                    # Match! Grab the untouched diagonal for free
                    dp[c] = prev
                else:
                    # Mismatch! min(Above, Left, Diagonal) + 1
                    dp[c] = 1 + min(dp[c], dp[c - 1], prev)
                    
                # 2. The old 'Above' value becomes the 'Diagonal' for the NEXT column
                prev = temp
                
        return dp[len1]