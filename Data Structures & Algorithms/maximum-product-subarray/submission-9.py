class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # edge cases
        if not nums:
            return 0
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # goal calc the max product at a given subarray
        # kadanes alg
        # keep track of 2 states local_max/local_min
        # we only care about the prev val so its doable in O(1) memory

        # define states + set them to the first val
        p_max = p_min = nums[0]
        res = float('-inf')
        for i in range(1, n):
            # at each point we are going to calc the states for a subarray ending at that index
            # We compare 3 vals 
            # Start a new subarry with just nums[i]
            # Add the current val to the current chain nums[i] * p_max
            # or check if the curr val will flip the min due to - - = +

            # do we choose to extend the chain or not
            # we extend it if 
            # extend_tot = max(nums[i] * p_max, nums[i] * p_min)
            # new_tot = nums[i]
            
            # c_max = c_min = nums[i]
            
            # if the new tot is greater we dont extend and lost old min/max
            # if extend_tot >= new_tot:
            c_max = max(nums[i], nums[i] * p_max, nums[i] * p_min)
            c_min = min(nums[i], nums[i] * p_max, nums[i] * p_min)

            p_max = c_max
            p_min = c_min

            res = max(p_max, res)
        
        return res
        
        

        