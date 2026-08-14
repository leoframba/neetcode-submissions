from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # sliding window
        # smallest possible window
        # dynamic window -> increase untill we find all vals and then shrink

        # len of the current window
        wlen = 0
        # count of the current vals in the window
        # ? do we need to track non-s vals
        target_counts = Counter(t)
        counts = Counter()

        # pointers
        l = 0
        r = 0

        n = len(s)
        ressize = float('inf')
        res = ""
        while r < n:
            # goal increase the window until we find a valid one
            cr = s[r]
            counts[cr] = counts.get(cr, 0) + 1

            isValid = target_counts <= counts
            if isValid:
                # attempt to shrink
                # we can move left if we dont need the val to be valid
                # 1) if its not in t
                # 2) if we have excess duplicates
                while s[l] not in target_counts or counts[s[l]] > target_counts[s[l]]:
                    counts[s[l]] -= 1
                    if counts[s[l]] == 0:
                        del counts[s[l]]
                    l += 1
                # after we've shrunk as much as possible set res
                window_len = r - l + 1
                if window_len < ressize:
                    ressize = window_len
                    res = s[l:r + 1] 
                

            r += 1 
        
        return res



        