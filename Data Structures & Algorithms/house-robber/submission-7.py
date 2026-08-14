class Solution:
    def rob(self, nums: List[int]) -> int:

        # cant rob adj houses
        
        cache = [-1] * len(nums)
        def dp(i) -> int:
            # wall
            # end of the neighborhood - 0 value from no house
            if i >= len(nums):
                return 0

            # if we have already calc'd this val use cache
            if cache[i] != -1:
                return cache[i]

            # what is the problem/choice
            # at any given index we can rob the current house or its adj
            # ie we need to find the max of robbing everything up to this point or eveything up till the prev point
            rob_current = nums[i] + dp(i + 2) # if we rob the current house we cannot rob the next
            skip = dp(i + 1) # we can skip this house to instead rob the next one

            #we wont the max value choice
            choice = max(skip, rob_current)
            cache[i] = choice
            return choice
        
        return dp(0)
        