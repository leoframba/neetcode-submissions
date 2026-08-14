class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # edge case
        # Empty list
        if n == 0:
            return 0 # no houses to rob
        if n == 1:
            return nums[0] # only one house to rob
        
        def rob_list(house_vals):
            # we only ever care about the values of the last two houses to calc the curr
            p1 = 0 # the val of the prev 1 house
            p2 = 0 # the val of the prev 2 house

            for val in house_vals:
                #calc the cost of the current house
                curr = max(val + p2, p1)
                
                # bump vals up 1 to handle next house
                p2 = p1
                p1 = curr

            return p1 # return the last curr

        #create the two differnt senarios

        # we either take house 1 and ignore the last house
        run1 = rob_list(nums[1:])
        run2 = rob_list(nums[:n - 1])

        return max(run1, run2)



        