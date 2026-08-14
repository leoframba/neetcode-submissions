from collections import Counter

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        tot = sum(n for n in nums)
        
        if tot % 2 != 0:
            return False

        # Each subarray must == target
        target = tot / 2
        # Problem becomes can we get to target with any numbers in the array. If we can the remaining numbers will be =
        # top down start from target and reduce
        counts = Counter(nums)
        def backtrack(curr) -> bool: # return = can we hit the target
            # wall
            if curr == 0:
                return True
            if curr < 0:
                return False

            # if theres still remaining target 
            for n in nums:
                if counts[n] > 0:
                    counts[n] -= 1
                    if backtrack(curr - n):
                        return True
                    counts[n] += 1 # backtrack
            
            return False 

        return backtrack(target)
        