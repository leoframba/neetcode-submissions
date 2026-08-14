from collections import Counter, deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # define the window
        l = 0
        r = 0

        n = len(nums)
        res = []
        # we will store tuples of (val, idx)
        mono = deque()
        # brute force
        # How do we track the state of the window?
        # Counts? - n to find new max
        # maxheap

        n = len(nums)
        while r < n:
            nr = nums[r]
            # pop all vals that are less than our current or their idx is out of window range
            if mono and (mono[0][1] < l):
                mono.popleft()

            while mono and mono[-1][0] <= nr:
                mono.pop()
            mono.append((nr, r))

            at_wsize = r - l + 1 == k
            if at_wsize:
                # we are at windowsize
                res.append(mono[0][0])
                l += 1
            r += 1
        
        return res
            
        
            
        