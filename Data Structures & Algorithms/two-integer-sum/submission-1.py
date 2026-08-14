class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            r = target - n
            if n in map:
                return [map[n], i]
            map[r] = i

        return [0, 0]
            
        