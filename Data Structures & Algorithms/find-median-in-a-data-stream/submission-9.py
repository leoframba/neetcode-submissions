import heapq

class MedianFinder:
    def __init__(self):
        self.minheap = []  # Holds the top half (larger numbers)
        self.maxheap = []  # Holds the bottom half (smaller numbers)

    def addNum(self, num: int) -> None:
        # 1. Default: push to the lower half
        heapq.heappush(self.maxheap, -num)
        
        # 2. Guarantee order: The largest element in the lower half 
        # must be moved to the upper half to ensure lower < upper
        trans = -heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap, trans)
        
        # 3. Balance: We arbitrarily choose to let maxheap be the larger one 
        # if the total count is odd.
        if len(self.minheap) > len(self.maxheap):
            trans = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -trans)

    def findMedian(self) -> float:
        # If sizes are unequal, maxheap has the extra element (the median)
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        
        # If sizes are equal, average the two roots
        return (-self.maxheap[0] + self.minheap[0]) / 2.0