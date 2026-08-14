# n * m * n solution 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        if not s:
            return True
        if not wordDict:
            return False
        
        n = len(s)
        wordset = set(wordDict)

        cache = {}
        def dp(start):
            for word in wordset:
                if start == n:
                    return True
                
                if start in cache:
                    return cache[start]
                
                word_len = len(word)
                curr = s[start: start + word_len]

                if curr == word and dp(start + word_len): # endgame we are done
                    return True # break

            cache[start] = False   
            return False # we've gone through the entire dict and havent found a valid word

        return dp(0)
        

        