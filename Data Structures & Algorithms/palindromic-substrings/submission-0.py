class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)

        res = 0

        for i in range(n):
            # odd pali case
            l = i
            r = i
            # while we are in range and still a valid pali
            while l >= 0 and r < n and s[l] == s[r]:
                # we have found a pali
                res += 1
                l -= 1
                r += 1
            
            # even case
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                    # we have found a pali
                    res += 1
                    l -= 1
                    r += 1
        
        return res