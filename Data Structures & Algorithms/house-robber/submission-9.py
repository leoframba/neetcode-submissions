class Solution:
    def rob(self, nums: List[int]) -> int:

        # iterative bottoms up


        # base case - where we start
        prevprev = 0
        prev = 0

        for i in range(len(nums)):
            # at any given point we are calc what the value UP UNTIL THIS POINT

            # if we choose to rob the current house we use -2
            rob_current = prevprev + nums[i]
            skip = prev

            # new - 2
            prevprev = prev
            # new - 1
            prev = max(skip, rob_current)
        return max(prev, prevprev)

        