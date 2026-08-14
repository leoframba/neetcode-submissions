class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # base cases for cheeky inputs
        if not s:
            return 0
        if n == 1:
            return 1
        dp = {}

        def is_pali(left, right):
             

            # check bounds
            if left >= right:
                return True 

            # if we havent already calc -> calc it
            if (left, right) not in dp:
                # check to see if ends are ==
                if s[left] == s[right]:
                    dp[(left, right)] = is_pali(left + 1, right -1) # if the outer vals are pali we must check inward
                else:
                    dp[(left, right)] = False

            return dp[left, right] 
        
        count = 0
        for i in range(n):
            for j in range(i, n):
                if is_pali(i, j):
                    count += 1
        return count
            



        