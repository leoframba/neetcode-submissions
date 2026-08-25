from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)

        if any(True 
            for val in counts.values()
            if val >= 2  
        ):
            return True

        return False
        