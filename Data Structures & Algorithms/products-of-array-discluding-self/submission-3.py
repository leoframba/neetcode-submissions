class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        tot = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                continue
            tot *= nums[i]
            

        if zero_count == 0:
            nums = [int(tot / n) for n in nums]
        
        if zero_count > 0:

            #case 1 zero
             for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = 0
                elif zero_count == 1:
                    nums[i] = tot
                    

    
        return nums
        