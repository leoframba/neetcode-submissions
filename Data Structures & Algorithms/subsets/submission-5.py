class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        #iterative

        #need to track states
        # state = idx/curr subset

        # define stack with starting state
        start_state = (0, [])
        stack = [start_state]
        res = []

        while stack:
            
            idx, ss = stack.pop()

            if idx >= len(nums):
                res.append(ss)
                continue
            
            # include
            stack.append((idx + 1, ss + [nums[idx]]))

            #exclude
            stack.append((idx + 1, ss))
        
        return res
            
            

            
            
            

        
        