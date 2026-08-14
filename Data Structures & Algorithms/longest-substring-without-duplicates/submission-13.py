class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        f = 0
        r = 0
        sub = {}

        while r < len(s):
            c = s[r]

            if c in sub and sub[c] >= f:
                f = sub[c] + 1 # set the front

            sub[c] = r
            longest = max(longest, r - f + 1)
            r += 1
        return longest