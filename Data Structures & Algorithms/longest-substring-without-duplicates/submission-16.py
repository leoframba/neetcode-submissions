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
            if c not in cmap:
                cmap[c] = right
                res = max(res, len(cmap)) # check if we got a new max bc we added
            else:
                # if we already have it - slide left until we have a valid seq again
                # we start at left and remove vals until we hit the repeated
                delta = (cmap[c] - left) + 1
                for i in range(left, left + delta):
                    cmap.pop(s[i])
                left += delta
                cmap[c] = right # set new

            right += 1
        return res
              
        


        