import heapq
class MedianFinder:

    def __init__(self):
        self.nums = []
        self.size = 0
        self.minheap = [] # hols the top half of nums
        self.maxheap = [] # holds the bottom half
        

    def addNum(self, num: int) -> None:
        if len(self.maxheap) == 0:
            heapq.heappush(self.minheap, num)
        else:
            # heaps must stay balanced at all times - never have a difference of more than 1
            peek_min = self.minheap[0]
            peek_max = -self.maxheap[0]

            if num < peek_max:
                heapq.heappush(self.maxheap, -num)

            if peek_max <= num <= peek_min:
                heapq.heappush(self.maxheap, -num)

            if peek_min < num:
                heapq.heappush(self.minheap, num)
        
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
        
        
        