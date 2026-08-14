class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = 0
        product = 1
        for e in nums:
            if e == 0 :
                zero += 1
            else:
                product *= e
        
        for i, e in enumerate(nums):
            if zero > 1:
                nums[i] = 0
            elif zero == 1:
                if e == 0:
                    nums[i] = product
                else:
                    nums[i] = 0
            else:           
                nums[i] = int(product / nums[i])

        return nums
        