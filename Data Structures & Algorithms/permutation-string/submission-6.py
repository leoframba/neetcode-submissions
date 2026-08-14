from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # sliding window

        #window is fixed - valid permutations must be the same size so our window should always be size of s1
        n1 = len(s1)
        n2 = len(s2)
        #edge to have a valid permu we must a larger n2
        if n1 > n2:
            return False
        
        # window starts at max
        l = 0
        r = 0

        # permutations need to have the same chars
        # keep track of current chars in window using a map
        #wcounts = {}
        tcounts = Counter(s1)
        currcounts = tcounts.copy()
        while r < n2:
            
            curr = s2[r]
            if curr in currcounts:
                # we've found a char in the permutation
                # check if we have room for it
                if currcounts[curr] > 0:
                    # we have room - compensate and check if we've hit the right le
                    currcounts[curr] -= 1 # remove it from the target
                    if r - l + 1 == n1:
                        return True
                else:
                    # we dont have room for it - slide window till we do
                    while currcounts[curr] == 0:
                        lcurr = s2[l]
                        currcounts[lcurr] += 1
                        l += 1
                    currcounts[curr] -= 1
            else:
                # permutations cannot contain invalid chars we reset
                l = r + 1
                currcounts = tcounts.copy()
                # need to reset map

            r += 1 

        return False