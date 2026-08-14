class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # edge case
        # Empty list
        if n == 0:
            return 0 # no houses to rob
        if n == 1:
            return nums[0] # only one house to rob
        
        def rob_list(start, stop):
            # we only ever care about the values of the last two houses to calc the curr
            p1 = 0 # the val of the prev 1 house
            p2 = 0 # the val of the prev 2 house

            for i in range(start, stop):
                #calc the cost of the current house
                curr = max(nums[i] + p2, p1)
                
                # bump vals up 1 to handle next house
                p2 = p1
                p1 = curr

            return p1 # return the last curr

        #create the two differnt senarios

        # we either take house 1 and ignore the last house
        run1 = rob_list(1, n) # avoid slice due to creating new 
        run2 = rob_list(0, n - 1)

        return max(run1, run2)



        