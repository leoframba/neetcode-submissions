class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        if not s:
            return 0

        #left defines the start of the seq
        left = 0
        #right defines the end
        right = 1

        n = len(s)

        # we are going to use a map to keep track of our subseq set
        # key = char : value : its index
        cmap = {s[0] : 0}

        res = 1
        while right < n:
            c = s[right]
            #check if we can add the new char to our seq
            if c in cmap and cmap[c] >= left:
                left = cmap[c] + 1

            res = max(res, (right - left) + 1)
            cmap[c] = right
            right += 1
        return res
              
        


        