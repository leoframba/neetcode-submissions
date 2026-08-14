# brute banner
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # edge cases
        # empty dict
        if not wordDict:
            return False
        
        # an empty string 
        if not s:
            return True
        
        n = len(s)
        wordSet = set(wordDict) # O(d) - where d where d is the size of wordDict
        # simple backtrack

        cache = {}
        # O(n^2) If we have to back track at every single letter
        def backtrack(start):
            # wall
            if start == n:
                return True
            
            if start in cache:
                return cache[start]
            
            for i in range(start, n):
                curr = s[start:i + 1]
                if curr in wordSet:
                    if backtrack(i + 1):
                        cache[start] = True 
                        return True

            cache[start] = False
            return False
        

        return backtrack(0)
        