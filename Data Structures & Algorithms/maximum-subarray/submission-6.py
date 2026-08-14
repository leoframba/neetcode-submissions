class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        largest_sum = float('-inf')
        for i in range(n): #start
            curr = nums[i]
            largest_sum = max(curr, largest_sum)
            for j in range(i + 1, n): #end
                curr += nums[j]
                largest_sum = max(curr, largest_sum)
        return largest_sum

        