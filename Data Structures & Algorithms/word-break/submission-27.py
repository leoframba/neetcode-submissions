class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # a empty string is technically split
        if not s:
            return True
        
        wordDict = set(wordDict)
        lenList = sorted(set(len(word) for word in wordDict))
        
        # the base case is a fully broken word when we reach the end
        # start from base case and work back

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        # calc each state
        for i in range(len(s) - 1, -1, -1):

            # we use the same logic as top down
            for l in lenList:
                if len(s) - i < l:
                    break
                
                if s[i:i+l] in wordDict and dp[i + l]:
                    dp[i] = True
                    break

        return dp[0]
        

        