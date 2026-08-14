class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # edge - empty nums
        if not nums:
            return 0

        # set our vals
        running_max = nums[0] # pos max
        running_min = nums[0] # negative max
        max_product = nums[0] # all time max ie res


        for i in range(1, len(nums)):

            # the runnin max - handles 0
            # we can start a new one if the current val is >
            # we can continue the subarray if the new value + the product
            # we can use the running_min if it flips too pos
            prev_rm = running_max
            running_max = max(nums[i], running_max * nums[i], running_min * nums[i])
            running_min = min(nums[i], prev_rm * nums[i], running_min * nums[i])
            
            
            max_product = max(max_product, running_max)
        
        return max_product