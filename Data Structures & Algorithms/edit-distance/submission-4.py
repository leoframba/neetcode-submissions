from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # edge
        #empty inpurt
        if not word1:
            return len(word2)
        
        if not word2:
            return len(word1)

        if not word1 and not word2:
            return 0

        if word1 == word2:
            return 0
        
        len1 = len(word1)
        len2 = len(word2)

        
        # track pos in each word
        @cache
        def dp(i1, i2):
            #wall 
            # end of word 2
            if i2 == len2:
                return len1 - i1 # delete the rest of i1
            
            if i1 == len1:
                return len2 - i2 # create the rest of i2
            
            # choice - preform op or not
            ops = float('inf')
            
            # if the two curr chars are == we can do nothing
            if word1[i1] == word2[i2]:
                ops = min(ops, dp(i1 + 1, i2 + 1))
            else: 
                ops = min(ops, dp(i1 + 1, i2 + 1) + 1) # Replace curr char with matching word2
                
                ops = min(ops, dp(i1 + 1, i2) + 1) # delete - we delete a char in s1 to skip it

                ops = min(ops, dp(i1, i2 + 1) + 1) # create
                
            
            return ops

        
        return dp(0, 0)

        