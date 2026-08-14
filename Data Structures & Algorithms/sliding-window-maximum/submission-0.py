from collections import Counter
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # define the window
        l = 0
        r = k

        n = len(nums)
        res = []
        # keep rolling max
        while r <= n:
            res.append(max(nums[l:r]))
            r += 1
            l += 1
        
        return res
                

            
            
            



        