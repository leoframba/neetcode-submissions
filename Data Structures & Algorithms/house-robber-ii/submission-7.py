class Solution:
    def rob(self, nums: List[int]) -> int:


        # edge - no houses to rob :(
        if not nums:
            return 0
        # edge - one house ez choice
        if len(nums) == 1:
            return nums[0] 
        
        # how to handle circle?
        # If we choose house 1 we cannot have house n-1
        

        def rob_from(start: int, end: int) -> int:
            prevprev = 0
            prev = 0

            # we use slice start/end so no +1
            for i in range(start, end):
                # choice 
                rob_current = nums[i] + prevprev
                skip = prev

                prevprev = prev
                prev = max(skip, rob_current)
        
            return max(prev, prevprev)
        
        return max(
            rob_from(0, len(nums) - 1), # we take house 0 so we exclude n - 1
            rob_from(1, len(nums))     # we take house n - 1 so we exclude 0
        )
