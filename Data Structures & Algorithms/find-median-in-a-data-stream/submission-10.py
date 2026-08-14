import heapq
class MedianFinder:

    def __init__(self):
        self.nums = []
        self.size = 0
        self.minheap = [] # hols the top half of nums
        self.maxheap = [] # holds the bottom half
        

    def addNum(self, num: int) -> None:
        
        #always push into lower
        heapq.heappush(self.minheap, num)

        #check if we need to balance
        if len(self.maxheap) > 0 and -self.maxheap[0] > self.minheap[0]:
            trans = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -trans)

        self.size += 1
        even = self.size % 2 == 0

        #balance if even
        min_size = len(self.minheap)
        max_size = len(self.maxheap)

        if even:
            while len(self.minheap) > len(self.maxheap):
                trans = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -trans)
            while len(self.minheap) < len(self.maxheap):
                trans = -heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, trans)
        
    def findMedian(self) -> float:
        even = self.size % 2 == 0

        if even:
            return (self.minheap[0] + -self.maxheap[0]) / 2
        else:
            return self.minheap[0] if len(self.minheap) > len(self.maxheap) else -self.maxheap[0]
        
        
        