class Solution:
    def findMin(self, nums: List[int]) -> int:

        f = 0
        r = len(nums) - 1

        while f < r:
            m = (r + f) // 2
            cur = nums[m]
            cur_f = nums[f]
            cur_r = nums[r]

            if cur > nums[r]:
                f = m + 1
            else:
                r = m
        
        return nums[r]
        


            


        