from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(nums)
        print(nums)

        maxi = 1
        curr = 1
        prev = nums[0]
        for i in range(len(nums)):
            if nums[i] - 1 == prev:
                curr += 1
                prev = nums[i]
                maxi = max(maxi, curr)
            elif nums[i] == prev:
                continue
            else:
                curr = 1
                prev = nums[i]
        
        return maxi
            



        