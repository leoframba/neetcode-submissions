class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        # prefix/postfix
        
        # pre
        res = [1] * len(nums)
        prefix = 1
        for i, e in enumerate(nums):
            res[i] = prefix
            prefix *= e
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        

        return res
        