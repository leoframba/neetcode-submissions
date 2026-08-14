class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        if len(s) == 0:
            return longest

        f = 0
        r = f + 1
        sub = set({s[f]})

        while r < len(s):
            if s[r] in sub:
                while s[f] != s[r]:
                    sub.remove(s[f])
                    f += 1
                f += 1
            else:
                sub.add(s[r])
                longest = max(longest, len(sub))
            r += 1
        longest = max(longest, len(sub))
        return longest