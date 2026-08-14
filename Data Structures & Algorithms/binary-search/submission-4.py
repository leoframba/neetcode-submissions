class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums: 
            return -1
        
        # two pointers
        f = 0
        r = len(nums) - 1

        while f <= r:
            mid = (f + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                f = mid + 1
        return -1
             
