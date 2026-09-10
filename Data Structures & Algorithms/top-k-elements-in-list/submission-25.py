from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        

        # create a list of tuple counts
        counts = [(value, key) for key, value in Counter(nums).items()]

        heap = counts[:k]
        print(heap)
        heapq.heapify(heap)
        for count, key in counts[k:]:
            # if we are full + find a value larger
            if len(heap) >= k and heap[0][0] < count:
                heapq.heapreplace(heap, (count, key))
        
        print(heap)
        return [key for _, key in heap]
        
        