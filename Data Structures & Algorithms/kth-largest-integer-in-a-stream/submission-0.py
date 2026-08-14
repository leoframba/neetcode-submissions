import bisect
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k
        

    def add(self, val: int) -> int:
        i = bisect.bisect_left(self.nums, val)
        self.nums = self.nums[:i] + [val] + self.nums[i:]
        print(self.nums)
        return self.nums[-self.k]
        
        
