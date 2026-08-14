class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = set()
        for i in range(n - 2):
            numi = nums[i]

            left = i + 1
            right = n - 1

            
            # move right pointer to lower val
            while left < right:
                curr = numi + nums[left] + nums[right]
                if curr == 0:
                    res.add(tuple([numi, nums[left], nums[right]]))
                    right -= 1
                    left += 1
                elif curr > 0:
                    right -= 1
                else:
                    left += 1
            
        return [list(item) for item in res]
        