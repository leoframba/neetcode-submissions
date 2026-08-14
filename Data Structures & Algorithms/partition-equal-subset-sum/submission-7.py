class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # An empty list of sum 0 can always be made with two subssets of 0
        if not nums:
            return True

        # we need to split the array into two equal vals
        # find the target val
        
        tot = sum(nums)
        # edge case - odd sum makes it imposible to have two = subsets
        if tot % 2 != 0:
            return False
        
        # if we can create a subset of this value the remaining vals will be the same
        target = tot // 2

        # generate subsets
        def gen_ss(start, tot) -> bool:
            if tot == target:
                return True
            
            if tot > target:
                return False
            
            for i in range(start, len(nums)):
                if gen_ss(i + 1, tot + nums[i]):
                    return True
                
            return False
        
        return gen_ss(0, 0)

        