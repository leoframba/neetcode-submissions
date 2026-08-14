from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #edge cases

        # we have an empty target but chars in one of our string
        if not s3 and (s1 or s2):
            return False
        
        if not s1 and not s2 and not s3:
            return True
        
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        # we cannot create len3 if we dont have enough chars
        if len3 != len1 + len2:
            return False

        # dp - Track 3 index based on where we are in each string
        @cache
        def dp(i1, i2, i3):
            # wall 
            # if we hit the end of one of our builder strings the remainder of the other string MUST == the remainder of l3
            if i1 == len1:
                return s2[i2:] == s3[i3:]
            if i2 == len2:
                return s1[i1:] == s3[i3:]
            # we should never hit the end of i3 before i1/i2

            # choice - Do we take a substring of 1 or 2 after that we must interchange
            # how do we decide how much to take?
            # look at first char

            # check both options
            op1 = False
            if s1[i1] == s3[i3]:
                op1 = dp(i1 + 1, i2, i3 + 1)
            op2 = False
            if s2[i2] == s3[i3]:
                op2 = dp(i1, i2 + 1, i3 + 1)

            return op1 or op2


        return dp(0, 0, 0)
        
        