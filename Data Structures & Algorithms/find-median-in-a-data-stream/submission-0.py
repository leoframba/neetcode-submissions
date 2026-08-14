import bisect
class MedianFinder:

    def __init__(self):
        self.nums = []
        self.size = 0
        

    def addNum(self, num: int) -> None:
        self.size += 1
        bisect.insort(self.nums, num)

        

    def findMedian(self) -> float:
        if self.size == 0:
            return float('-inf')
        
        even = self.size % 2 == 0

        # ass sorted list
        mididx = (self.size // 2) - 1
        if even:
            return (self.nums[mididx + 1] + self.nums[mididx]) / 2
        else:
            return self.nums[mididx + 1]
        
        