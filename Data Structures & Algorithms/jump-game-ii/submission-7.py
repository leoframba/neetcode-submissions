class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_jump_end = 0
        farthest = 0
        
        # We loop up to len(nums) - 1 because we don't need to jump 
        # again if we are already standing on the last index.
        for i in range(len(nums) - 1):
            
            # 1. Continually find the farthest we can reach from our current window
            farthest = max(farthest, i + nums[i])
            
            # 2. If we have hit the end of our current jump's radius...
            if i == current_jump_end:
                jumps += 1                  # We are forced to take a jump
                current_jump_end = farthest # Our new radius expands
                
        return jumps