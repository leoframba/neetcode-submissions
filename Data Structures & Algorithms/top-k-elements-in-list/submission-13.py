from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #edge cases
        #empty input
        n = len(nums)
        if n <= k:
            return nums

        #brute force
        counts = Counter(nums)
        maxheap = []

        for key, val in counts.items():
            heapq.heappush(maxheap, (-val, key))
        
        return [heapq.heappop(maxheap)[1] for _ in range(k)]




        