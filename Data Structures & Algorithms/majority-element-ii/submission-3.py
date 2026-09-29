class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        v1 = None
        count2 = 0
        v2 = None

        for i in range(len(nums)):
            if count1 == 0:
                v1 = nums[i]
                count1 += 1
                continue
            
            if count2 == 0 and nums[i] != v1:
                v2 = nums[i]
                count2 += 1
                continue
            
            curr = nums[i]
            if v1 == curr:
                count1 += 1
            elif v2 == curr:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        res = []
        if sum(1 for num in nums if num == v1) > len(nums) // 3:
            res.append(v1)
        if sum(1 for num in nums if num == v2) > len(nums) // 3:
            res.append(v2)
        return res




        