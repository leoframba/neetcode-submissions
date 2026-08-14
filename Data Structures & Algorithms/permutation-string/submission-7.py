from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # sliding window
        # fixed window - permutation must be same len

        n1 = len(s1)
        n2 = len(s2)
        # a perm cant exist if the other is smaller
        if n1 > n2:
            return False
        
        counts1 = Counter(s1)
        counts2 = Counter(s2[:n1 - 1])

        l = 0
        r = n1 - 1

        while r < n2:
            sr = s2[r]
            counts2[sr] = counts2.get(sr, 0) + 1
            if counts1 == counts2:
                return True
            
            # slide window remove left
            sl = s2[l]
            counts2[sl] -= 1
            if counts2[sl] == 0:
                counts2.pop(sl) 
            l += 1
            r += 1
        return False
            
        