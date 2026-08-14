import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        maxheap = stones
        heapq.heapify(maxheap)

        # while we have two stones to smash
        while len(maxheap) >= 2:
            y = -heapq.heappop(maxheap)
            x = -heapq.heappop(maxheap)
            smash = y - x
            if smash > 0:
                heapq.heappush(maxheap, -smash)
        
        return 0 if not maxheap else -maxheap[0]

        
        