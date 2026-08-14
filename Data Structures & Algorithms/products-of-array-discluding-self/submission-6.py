class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # iterate through array to calc each val

        # we can do a pass to total the array
        product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else: 
                product *= num
        
        # tricky part is 0s
        # one zero and we need to calc 
        
        if zero_count >= 2:
            return [0] * len(nums)
        elif zero_count == 1:
            return [0 if num != 0 else product for num in nums]
        else:
            return [product // num for num in nums]
        
        
        