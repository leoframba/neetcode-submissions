from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_counts = Counter(t)
        counts = Counter()

        l = 0
        ressize = float('inf')
        res = ""
        
        have = 0
        # need is the number of UNIQUE characters we must fulfill
        need = len(target_counts) 

        for r in range(len(s)):
            cr = s[r]
            counts[cr] += 1

            # 1. Did we just fulfill the requirement for this specific character?
            if cr in target_counts and counts[cr] == target_counts[cr]:
                have += 1

            # 2. While the window is perfectly valid, try to shrink it
            while have == need:
                # Save the smallest valid window
                window_len = r - l + 1
                if window_len < ressize:
                    ressize = window_len
                    res = s[l:r + 1]
                
                # Pop the left character to shrink
                cl = s[l]
                counts[cl] -= 1
                
                # 3. Did removing this character break our requirement?
                if cl in target_counts and counts[cl] < target_counts[cl]:
                    have -= 1 # The window is now invalid, the while loop will exit
                    
                l += 1
                
        return res