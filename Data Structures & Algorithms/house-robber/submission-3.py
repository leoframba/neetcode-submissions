class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # everytime we look to rob a house we have to look at the oppurtunity cost
        # If we rob house a cost = (a - 1) + (a + 1)
        dp_opp = 0
        dp_prev = 0

        for i in range(n):
            # Edge - need to handle out of bounds

            # Calc the oppurtunity cost
            opp_idx = i - 1
            opp_cost = 0
            # if we are in bounds - get the value from the costs/dp
            if 0 <= opp_idx:
                opp_cost = dp_opp
            
            # Calc the val of the current house
            p_idx = i - 2
            p_cost = 0
            # if we are inbounds
            if 0 <= p_idx:
                p_cost = dp_prev
            
            # current val vs taking the opp cost
            dp_opp = max(p_cost + nums[i], opp_cost)
            dp_prev = opp_cost

        return dp_opp



            

            

                

            


        