from collections import Counter
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # define the window
        l = 1
        r = k

        n = len(nums)
        res = []
        # brute force
        # How do we track the state of the window?
        # Counts? - n to find new max
        # maxheap

        maxheap = [-nums[i] for i in range(k)]
        # build the counts
        counts = Counter(nums[:k])
        # build the heap
        heapq.heapify(maxheap)

        res = []
        while r <= n:
            # at any given point our max is the
            while -maxheap[0] not in counts:
                # if the val isnt in counts its an old deleted val
                heapq.heappop(maxheap)
            
            res.append(-maxheap[0])

            # to prepare for the next window we need to add r and remove l
            # We cant remove from a heap so we remove it from counts and validate our pops
            nl = nums[l - 1]
            counts[nl] -= 1
            if counts[nl] == 0:
                del counts[nl]
            
            # add new r if r in range
            if r < n:
                nr = nums[r]
                heapq.heappush(maxheap, -nr)
                counts[nr] = counts.get(nr, 0) + 1

            l, r = l + 1, r + 1
        return res
                

            
            
            



        