class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = {}
        # look at the ends of a substring and then check if middle is already a pali
        def is_pal(left, right):
            
            # base case for 1 or 0 len string
            if left >= right:
                return True
            
            #check if in memo
            if (left, right) not in memo:
                if s[left] == s[right]: # if the outer is a match we check the inner
                    memo[(left, right)] = is_pal(left + 1, right - 1)
                else:
                    # if no match
                    memo[left, right] = False


            return memo[(left, right)]
            

        res_start = 0
        res_max_len = 0

        for i in range(n):
            for j in range(i, n): #start from i to check single chars
                if is_pal(i, j):
                    curr_len = j - i + 1
                    if curr_len > res_max_len:
                        res_max_len = curr_len
                        res_start = i
        
        return s[res_start : res_start + res_max_len]

        