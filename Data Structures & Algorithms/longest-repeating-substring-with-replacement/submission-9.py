class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # slidig window

        l = 0
        r = 0
        # window state = window counts
        counts = {}

        n = len(s)
        res = 0
        while r < n:
            curr = s[r]
            # add the new val to the window
            counts[curr] = counts.get(curr, 0) + 1
            #validation
            window_len = (r - l) + 1
            # the max val is the main val
            replacements = window_len - max(counts.values())

            if replacements > k:
                # slide the window start left
                counts[s[l]] -= 1
                l += 1
            else:
                res = max(res, window_len)
                #keep looking right
            
            # always move r
            r += 1
        
        return res
            
        
        