import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        def quick_select(nums, k):
        
            pivot = random.choice(nums)

            left = [x for x in nums if x > pivot]
            mid = [x for x in nums if x == pivot]
            right = [x for x in nums if x < pivot]

            L, M = len(left), len(mid)

            if k <= L:
                return quick_select(left, k)
            elif k <= L + M:
                return pivot
            else:
                return quick_select(right, k - L - M)
            
        return quick_select(nums, k)
                