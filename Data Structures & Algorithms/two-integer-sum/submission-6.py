class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # map of Key = remainder to reach target , Value = Index of the other num
        targets = {}

        for i in range(len(nums)):
            remainder = target - nums[i]

            if nums[i] in targets:
                return [targets[nums[i]], i]
            else:
                targets[remainder] = i
        
        # didnt find 
        return None

            
        