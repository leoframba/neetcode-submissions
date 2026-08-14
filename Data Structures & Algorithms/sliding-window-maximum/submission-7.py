from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        n = len(nums)
        res = []
        mono = deque() # strictly storing indices now

        while r < n:
            nr = nums[r]
            
            # pop all vals that are out of window range
            if mono and mono[0] < l:
                mono.popleft()

            # pop all vals that are smaller than current
            while mono and nums[mono[-1]] <= nr:
                mono.pop()
                
            mono.append(r)

            if r - l + 1 == k:
                # the max is the value at the index stored at the front
                res.append(nums[mono[0]])
                l += 1
                
            r += 1
        
        return res