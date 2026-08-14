import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # convert to min heap
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        self.k = k

        # get the size of heap to k
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        

    def add(self, val: int) -> int:
        
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        
        elif val > self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)
        
        return self.min_heap[0]
            
        
        
