from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        #edge case - empty s
        if not s:
            return True

        # brute force we can iterate over all substrings to see if they are valid words

        #convert wordDict to a set for faster lookups

        wordSet = set(wordDict)
        lenList = sorted(set(len(word) for word in wordSet))

        #top down
        # given a start index can we find a valid word
        @cache
        def dp(start) -> bool:
            # wall/base - end of string
            # if we get here we've found a valid word
            if start >= len(s):
                return True

            # at each state we are going to look for a valid word
            for l in lenList:
                if len(s) - start < l:
                    break
                if s[start: start + l] in wordSet and dp(start + l):
                    return True
            
            # no word found
            return False
        
        return dp(0)
                    

        