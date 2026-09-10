class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0

        product = 1
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
                continue
            product *= nums[i]

        # if we have 1 zero everything but the one zero is 0
        if zeros == 1:
            return [
                0 if num != 0 else product
                for num in nums
            ]
        # if we have more than one everything is 0
        if zeros >= 2:
            return [0] * len(nums)
        
        #if we have no zeros
        return [int(product / num) for num in nums]
        
        
        