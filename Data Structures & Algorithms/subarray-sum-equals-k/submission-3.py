class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_map = {0: 1}

        running_sum = 0
        res = 0
        for i in range(len(nums)):
            running_sum += nums[i]

            need = running_sum - k
            if need in prefix_map:
                res += prefix_map[need]
            
            if running_sum in prefix_map:
                prefix_map[running_sum] += 1
            else:
                prefix_map[running_sum] = 1
        
        return res
        