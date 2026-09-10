from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        

        # create a list of tuple counts
        counts = [(-v, k) for k, v in Counter(nums).items()]

        # create a max heap
        heapq.heapify(counts)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(counts)[1])
        
        return res
        
        