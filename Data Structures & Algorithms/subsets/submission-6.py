class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = [] # current array we are building

        def gen(i):
            # wall
            # out of bounds
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            # at any number we can include or skip
            
            curr.append(nums[i])
            gen(i + 1)

            # back track
            curr.pop()

            gen(i + 1)
        
        gen(0)
        return res 
            

        