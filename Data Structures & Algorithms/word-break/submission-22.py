from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        #edge case - empty s
        if not s:
            return True

        # brute force we can iterate over all substrings to see if they are valid words

        #convert wordDict to a set for faster lookups

        wordSet = set(wordDict)

        #top down
        # given a start index can we find a valid word
        @cache
        def dp(start) -> bool:
            # wall/base - end of string
            # if we get here we've found a valid word
            if start >= len(s):
                return True

            # at each state we are going to look for a valid word
            for i in range(start, len(s)):
                curr = s[start: i + 1] # n -- need to imporve this
                if curr in wordSet and dp(i + 1): # if we find a word + the rest of the word is good return True
                    return True
            
            # no word found
            return False
        
        return dp(0)
                    

        