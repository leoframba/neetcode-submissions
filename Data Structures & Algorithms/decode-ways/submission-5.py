class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if not s or s[0] == "0":
            return 0
        p1 = 1
        p2 = 1

        for i in range(1, n):
            curr = 0 
            # check if the single digit is a valid code
            if s[i] != "0":
                curr += p1
            
            # double digit check
            two_digits = int(s[i - 1: i+1])
            if 10 <= two_digits <= 26:
                curr += p2
            
            p2 = p1
            p1 = curr

        return p1 

            

        
        