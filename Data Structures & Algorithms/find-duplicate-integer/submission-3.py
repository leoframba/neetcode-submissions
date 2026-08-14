class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        f = nums[0]
        s = nums[0]

        while True:
            f = nums[nums[f]]
            s = nums[s]

            if f == s:
                break

        s = nums[0]
        while s != f:
            f = nums[f]
            s = nums[s]

        
        return f

        