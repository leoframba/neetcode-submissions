class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        def dp(start):
            if start >= n - 1:
                return True
            
            for i in range(nums[start], 0, -1):
                if dp(start + i):
                    return True
            
            return False
        
        return dp(0)
        