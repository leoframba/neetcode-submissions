class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        heap = []

        for key in counts:
            heapq.heappush(heap, (counts[key], key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        
        return [pair[1] for pair in heap]

        