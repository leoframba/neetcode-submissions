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
        cache = {}
        def gen_subsets(start, tot) -> bool:
            if tot == target:
                return True
            if tot > target or start >= len(nums):
                return False
            
            if (start, tot) in cache:
                return cache[(start, tot)]
            
            for i in range(start, len(nums)):
                if gen_subsets(i + 1, tot + nums[i]):
                    return True
            
            cache[(start, tot)] = False
            return False
        
        return gen_subsets(0, 0)

        