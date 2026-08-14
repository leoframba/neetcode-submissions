class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        f = 0
        r = 0
        sub = {}

        while r < len(s):
            if s[r] in sub:
                f = sub[s[r]] + 1 # set the front
                sub.clear() # clear the dict
                sub[s[f]] = f  # add 
                r = f
            else:
                sub[s[r]] = r
                longest = max(longest, len(sub))
            r += 1
        longest = max(longest, len(sub))
        return longest