class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        
        curr = res = nums[0]

        for i in range(1, len(nums)):
            if i > res:
                return False

            curr = i + nums[i]
            res = max(curr, res)

            if res >= len(nums) - 1: 
                return True
        
        return False
        



        