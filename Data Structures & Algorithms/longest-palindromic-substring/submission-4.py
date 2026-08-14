class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        res_len = 0

        # odd case (one middle char)
        # start from a char and exapnd out looking for pali
        for i in range(n):
            left = i
            right = i
            # continue to expand as long as we are a pali
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
                curr_size = right - left + 1
                if curr_size > res_len:
                    res = s[left + 1:right]
                    res_len = curr_size
        

        #even case (two middle chars)
        for i in range(n):
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
                curr_size = right - left + 1
                if curr_size > res_len:
                    res = s[left + 1: right]
                    res_len = curr_size

        return res
        