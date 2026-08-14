class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        
        res = []
        def gen(i, curr):

            if i >= len(nums):
                res.append(curr)
                return
            
            gen(i + 1, curr + [nums[i]])
            gen(i + 1, curr)
        
        gen(0, [])
        return res
