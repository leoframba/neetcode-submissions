class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # edge cases - empty nums:
        if not nums:
            return 0
        
        # edge case single nums:
        if len(nums) == 1:
            return nums[0]
        
        # Plan break the list into substrings. States will be left/right bounds
        # We have n^2 states as there are always n(n + 1)/2 possible substrings
        base = max(nums)
        cache = {}
        def dp(left, right):
            #prune 1s as they dont contribute too product
            while left < right and nums[left] == 1:
                left += 1
            while right > left and nums[right] == 1:
                right -= 1

            #wall single list cannot be broken down further
            state = (left, right)
            if left == right:
                cache[state] = nums[left]
                return nums[left]
            
            # if state is cached use cache
            if state in cache:
                return cache[state]

            product = 1
            # at each state we need to calc its product
            for i in range(left, right + 1):
                product *= nums[i]
            
            # is this states products the max compared to others
            # can prune by ignoring 1s?
            cut_l = dp(left + 1, right)
            cut_r = dp(left, right - 1)

            
            cache[state] = max(product, cut_l, cut_r)
            return cache[state]
        
        return max(dp(0, len(nums) - 1), base)

        