class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        largest_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, n): #start
            current_sum = max(nums[i], current_sum + nums[i])
            largest_sum = max(current_sum, largest_sum)
            
        return largest_sum

        