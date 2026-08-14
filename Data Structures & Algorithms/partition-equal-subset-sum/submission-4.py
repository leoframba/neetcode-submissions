from collections import Counter

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        tot = sum(n for n in nums)
        
        if tot % 2 != 0:
            return False
        n = len(nums)
        # Each subarray must == target
        target = tot / 2
        # Problem becomes can we get to target with any numbers in the array. If we can the remaining numbers will be =
        # top down start from target and reduce
        cache = {}
        def backtrack(start, curr) -> bool: # return = can we hit the target
            # wall
            if curr == 0:
                return True
            if curr < 0 or start == n:
                return False
            

            # include current            
            if backtrack(start + 1, curr - nums[start]):
                return True
            
            # or skip
            if backtrack(start + 1, curr):
                return True
            
            cache[start] = False
            return False 

        return backtrack(0, target)
        