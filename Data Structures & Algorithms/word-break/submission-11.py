class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return False
        if not s:
            return True

        n = len(s)        
        dp = [False] * (n + 1) # True if the word up to i can be segmented
        dp[0] = True # Empty string is always valid

        wordSet = set(wordDict)
        for end in range(1, n + 1): # the end boundry of the current prefix we are eval
            
            for split in range(end): # split point
                # 1) Is the word before end valid
                # 2) is the remaining post j also valid
                if dp[split] and s[split: end] in wordSet:
                    dp[end] = True
                    break
        
        return dp[n]
                    
    

        