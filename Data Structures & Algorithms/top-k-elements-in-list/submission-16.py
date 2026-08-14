from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #edge cases
        #empty input
        n = len(nums)
        if n <= k:
            return nums

        # create a dict of size nums
        counts = Counter(nums)
        minheap = []
        
        # push n items at logn cost each n log n
        for key, val in counts.items():
            heapq.heappush(minheap, (val, key))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        # k is const so no time
        return [tup[1] for tup in minheap]

        # Time O (n log n) - due to n heappush
        # Space O (n) We allocate a dict of size n and a heap of size n so 2n or n




        