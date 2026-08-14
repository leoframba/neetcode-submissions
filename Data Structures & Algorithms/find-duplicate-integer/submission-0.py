class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        numLen = len(nums)

        for i in range(numLen):
            cur = nums[i]
            cur = cur if cur >= 0 else -cur
            if nums[cur - 1] < 0:
                return cur
            else:
                nums[cur - 1] *= -1
        
        return -1



        