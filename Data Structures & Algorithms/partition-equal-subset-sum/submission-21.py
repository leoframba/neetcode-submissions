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
        cache = [False for _ in range(target + 1)]
        cache[0] = True # we can always reach 0
        
        # is this target reachable
        for num in nums:
            for tar in range(target, num - 1, -1):
                cache[tar] = cache[tar] or cache[tar - num]
        
        print(cache)
        return cache[target]
             


        